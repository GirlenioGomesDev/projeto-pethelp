from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CadastroUsuarioForm


class PetHelpLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm


def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, 'Conta criada com sucesso. Seja bem-vindo ao PetHelp!')
            return redirect('minhas_publicacoes')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'accounts/cadastro.html', {'form': form})
