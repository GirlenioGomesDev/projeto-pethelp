from django import forms

from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'nome',
            'categoria',
            'foto',
            'raca',
            'idade',
            'porte',
            'bairro',
            'cidade',
            'data_perdido',
            'caracteristicas',
            'telefone',
            'descricao',
        ]
        labels = {
            'raca': 'Raça',
            'data_perdido': 'Data em que desapareceu',
            'telefone': 'Número para contato',
        }
        widgets = {
            'data_perdido': forms.DateInput(attrs={'type': 'date'}),
            'caracteristicas': forms.Textarea(attrs={'rows': 4}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        data_perdido = cleaned_data.get('data_perdido')

        if categoria == 'perdido' and not data_perdido:
            self.add_error('data_perdido', 'Informe a data em que o pet desapareceu.')

        return cleaned_data
