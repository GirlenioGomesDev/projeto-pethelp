from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CadastroUsuarioForm, PublicacaoPetForm
from .models import PublicacaoPet


def pode_gerenciar(user, publicacao):
    return user.is_authenticated and (user == publicacao.usuario or user.is_superuser)


def filtrar_publicacoes(request, queryset=None):
    queryset = queryset or PublicacaoPet.objects.all()
    query = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    if query:
        queryset = queryset.filter(
            Q(nome__icontains=query)
            | Q(tipo_animal__icontains=query)
            | Q(bairro__icontains=query)
            | Q(caracteristicas__icontains=query)
            | Q(descricao__icontains=query)
        )
    if status in ['ativo', 'resolvido']:
        queryset = queryset.filter(status=status)

    return queryset


def home(request):
    publicacoes = filtrar_publicacoes(request)
    query = request.GET.get('q', '').strip()
    recentes = publicacoes if query else PublicacaoPet.objects.filter(status='ativo')[:6]

    contexto = {
        'total_perdidos': PublicacaoPet.objects.filter(categoria='perdido', status='ativo').count(),
        'total_encontrados': PublicacaoPet.objects.filter(categoria='encontrado', status='ativo').count(),
        'total_adocao': PublicacaoPet.objects.filter(categoria='adocao', status='ativo').count(),
        'total_resolvidos': PublicacaoPet.objects.filter(status='resolvido').count(),
        'recentes': recentes,
    }
    return render(request, 'animais/home.html', contexto)


def lista_categoria(request, categoria):
    titulos = {
        'perdido': 'Pets Perdidos',
        'encontrado': 'Patinhas Encontradas',
        'adocao': 'Adotar um Focinho',
    }
    publicacoes = filtrar_publicacoes(request, PublicacaoPet.objects.filter(categoria=categoria))
    return render(request, 'animais/lista.html', {
        'publicacoes': publicacoes,
        'titulo': titulos[categoria],
        'categoria': categoria,
    })


def detalhe_publicacao(request, pk):
    publicacao = get_object_or_404(PublicacaoPet, pk=pk)
    return render(request, 'animais/detalhe.html', {'publicacao': publicacao})


@login_required
def cadastrar_publicacao(request):
    categoria = request.GET.get('categoria')
    if request.method == 'POST':
        form = PublicacaoPetForm(request.POST, request.FILES)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.usuario = request.user
            publicacao.save()
            messages.success(request, 'Publicacao cadastrada com sucesso!')
            return redirect('minhas_publicacoes')
    else:
        form = PublicacaoPetForm(initial={'categoria': categoria} if categoria else None)
    return render(request, 'animais/form_publicacao.html', {'form': form, 'modo': 'criar'})


@login_required
def editar_publicacao(request, pk):
    publicacao = get_object_or_404(PublicacaoPet, pk=pk)
    if not pode_gerenciar(request.user, publicacao):
        messages.error(request, 'Voce nao tem permissao para editar essa publicacao.')
        return redirect('minhas_publicacoes')

    if request.method == 'POST':
        form = PublicacaoPetForm(request.POST, request.FILES, instance=publicacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicacao atualizada com sucesso!')
            return redirect('detalhe_publicacao', pk=publicacao.pk)
    else:
        form = PublicacaoPetForm(instance=publicacao)

    return render(request, 'animais/form_publicacao.html', {
        'form': form,
        'modo': 'editar',
        'publicacao': publicacao,
    })


@login_required
def minhas_publicacoes(request):
    if request.user.is_superuser:
        publicacoes = filtrar_publicacoes(request)
    else:
        publicacoes = filtrar_publicacoes(request, PublicacaoPet.objects.filter(usuario=request.user))
    return render(request, 'animais/minhas_publicacoes.html', {'publicacoes': publicacoes})


@login_required
def alternar_status_publicacao(request, pk):
    publicacao = get_object_or_404(PublicacaoPet, pk=pk)
    if not pode_gerenciar(request.user, publicacao):
        messages.error(request, 'Voce nao tem permissao para alterar essa publicacao.')
        return redirect('minhas_publicacoes')

    publicacao.status = 'ativo' if publicacao.status == 'resolvido' else 'resolvido'
    publicacao.save(update_fields=['status', 'atualizado_em'])
    messages.success(request, 'Status da publicacao atualizado.')
    return redirect('minhas_publicacoes')


@login_required
def apagar_publicacao(request, pk):
    publicacao = get_object_or_404(PublicacaoPet, pk=pk)
    if not pode_gerenciar(request.user, publicacao):
        messages.error(request, 'Voce nao tem permissao para apagar essa publicacao.')
        return redirect('minhas_publicacoes')
    if request.method == 'POST':
        publicacao.delete()
        messages.success(request, 'Publicacao apagada com sucesso!')
        return redirect('minhas_publicacoes')
    return render(request, 'animais/confirmar_apagar.html', {'publicacao': publicacao})


def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('minhas_publicacoes')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'animais/cadastro_usuario.html', {'form': form})


class PetHelpLoginView(LoginView):
    template_name = 'animais/login.html'
    authentication_form = AuthenticationForm
