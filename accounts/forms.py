from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    nome = forms.CharField(label='Nome', max_length=120)
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ['nome', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ja existe uma conta cadastrada com este e-mail.')
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.username = self.cleaned_data['email'].strip().lower()
        usuario.email = self.cleaned_data['email'].strip().lower()
        usuario.first_name = self.cleaned_data['nome'].strip()
        if commit:
            usuario.save()
        return usuario
