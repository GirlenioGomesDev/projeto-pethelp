from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import PublicacaoPet


class CadastroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='Nome')
    email = forms.EmailField(required=True, label='E-mail')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']
        labels = {'username': 'Usuario'}


class PublicacaoPetForm(forms.ModelForm):
    class Meta:
        model = PublicacaoPet
        fields = [
            'categoria',
            'foto',
            'nome',
            'tipo_animal',
            'caracteristicas',
            'contato',
            'data_perda',
            'bairro',
            'idade',
            'porte',
            'descricao',
        ]
        labels = {
            'nome': 'Nome do pet',
            'foto': 'Foto do pet',
            'contato': 'Numero para contato',
            'descricao': 'Descricao adicional',
        }
        widgets = {
            'data_perda': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'caracteristicas': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned = super().clean()
        categoria = cleaned.get('categoria')

        obrigatorios_por_categoria = {
            'perdido': [
                ('nome', 'Nome do pet e obrigatorio para pets perdidos.'),
                ('tipo_animal', 'Tipo do animal e obrigatorio para pets perdidos.'),
                ('caracteristicas', 'Caracteristicas peculiares sao obrigatorias.'),
                ('contato', 'Contato e obrigatorio para pets perdidos.'),
                ('data_perda', 'Informe o dia em que o pet foi perdido.'),
                ('bairro', 'Bairro e obrigatorio para pets perdidos.'),
            ],
            'encontrado': [
                ('bairro', 'Bairro e obrigatorio para patinhas encontradas.'),
                ('contato', 'Contato e obrigatorio para patinhas encontradas.'),
                ('caracteristicas', 'Caracteristicas sao obrigatorias para ajudar no reconhecimento.'),
                ('descricao', 'Descricao e obrigatoria para animais encontrados.'),
            ],
        }

        for campo, mensagem in obrigatorios_por_categoria.get(categoria, []):
            if not cleaned.get(campo):
                self.add_error(campo, mensagem)

        return cleaned
