from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PetForm
from .models import Pet


def pode_gerenciar(user, pet):
    # Dono da publicacao e equipe/admin podem moderar o conteudo.
    return user.is_authenticated and (user == pet.usuario or user.is_staff or user.is_superuser)


def filtrar_pets(request, queryset=None):
    queryset = queryset or Pet.objects.all()
    busca = request.GET.get('q', '').strip()
    bairro = request.GET.get('bairro', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    if busca:
        queryset = queryset.filter(
            Q(nome__icontains=busca)
            | Q(bairro__icontains=busca)
            | Q(cidade__icontains=busca)
            | Q(raca__icontains=busca)
            | Q(caracteristicas__icontains=busca)
        )
    if bairro:
        queryset = queryset.filter(bairro__icontains=bairro)
    if categoria in dict(Pet.CATEGORIAS):
        queryset = queryset.filter(categoria=categoria)

    return queryset


def home(request):
    pets = filtrar_pets(request)
    contexto = {
        'recentes': pets[:6],
        'total_perdidos': Pet.objects.filter(categoria='perdido').count(),
        'total_encontrados': Pet.objects.filter(categoria='encontrado').count(),
        'total_adocao': Pet.objects.filter(categoria='adocao').count(),
    }
    return render(request, 'pets/home.html', contexto)


def galeria(request):
    pets = filtrar_pets(request)
    return render(request, 'pets/galeria.html', {
        'pets': pets,
        'titulo': 'Galeria de Pets',
        'categoria_atual': request.GET.get('categoria', ''),
    })


def lista_categoria(request, categoria):
    titulos = {
        'perdido': 'Pet Perdidos',
        'encontrado': 'Patinhas Encontradas',
        'adocao': 'Adotar Focinho',
    }
    pets = filtrar_pets(request, Pet.objects.filter(categoria=categoria))
    return render(request, 'pets/galeria.html', {
        'pets': pets,
        'titulo': titulos[categoria],
        'categoria_atual': categoria,
    })


def detalhe_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/detalhe.html', {'pet': pet})


@login_required
def cadastrar_pet(request):
    categoria = request.GET.get('categoria')
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            messages.success(request, 'Pet cadastrado com sucesso no PetHelp.')
            return redirect('detalhe_pet', pk=pet.pk)
    else:
        form = PetForm(initial={'categoria': categoria} if categoria in dict(Pet.CATEGORIAS) else None)

    return render(request, 'pets/form.html', {'form': form, 'modo': 'criar'})


@login_required
def editar_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if not pode_gerenciar(request.user, pet):
        messages.error(request, 'Voce nao tem permissao para editar esta publicacao.')
        return redirect('detalhe_pet', pk=pet.pk)

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicacao atualizada com sucesso.')
            return redirect('detalhe_pet', pk=pet.pk)
    else:
        form = PetForm(instance=pet)

    return render(request, 'pets/form.html', {'form': form, 'modo': 'editar', 'pet': pet})


@login_required
def excluir_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if not pode_gerenciar(request.user, pet):
        messages.error(request, 'Voce nao tem permissao para excluir esta publicacao.')
        return redirect('detalhe_pet', pk=pet.pk)

    if request.method == 'POST':
        pet.delete()
        messages.success(request, 'Publicacao excluida com sucesso.')
        return redirect('minhas_publicacoes')

    return render(request, 'pets/confirmar_exclusao.html', {'pet': pet})


@login_required
def minhas_publicacoes(request):
    queryset = Pet.objects.all() if request.user.is_staff or request.user.is_superuser else Pet.objects.filter(usuario=request.user)
    return render(request, 'pets/minhas_publicacoes.html', {'pets': filtrar_pets(request, queryset)})
