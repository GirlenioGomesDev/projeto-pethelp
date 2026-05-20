import re

from django import forms

from .models import Pet


PET_DATE_LABELS = {
    'perdido': 'Data em que desapareceu',
    'encontrado': 'Data em que foi encontrado',
    'adocao': 'Data de entrada para adoção',
}


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
            'data_perdido': forms.DateInput(attrs={
                'type': 'date',
                'data-label-perdido': PET_DATE_LABELS['perdido'],
                'data-label-encontrado': PET_DATE_LABELS['encontrado'],
                'data-label-adocao': PET_DATE_LABELS['adocao'],
            }),
            'telefone': forms.TextInput(attrs={
                'inputmode': 'numeric',
                'autocomplete': 'tel',
                'maxlength': '15',
                'placeholder': '(99) 99999-9999',
                'pattern': r'\(\d{2}\) \d{5}-\d{4}',
                'title': 'Informe um telefone com DDD no formato (99) 99999-9999.',
            }),
            'caracteristicas': forms.Textarea(attrs={'rows': 4}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categoria = (
            self.data.get('categoria')
            or self.initial.get('categoria')
            or getattr(self.instance, 'categoria', None)
        )
        if categoria in PET_DATE_LABELS:
            self.fields['data_perdido'].label = PET_DATE_LABELS[categoria]

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone', '').strip()
        if telefone and not re.fullmatch(r'[\d\s().-]+', telefone):
            raise forms.ValidationError('Informe apenas números no telefone.')

        numeros = re.sub(r'\D', '', telefone)
        if len(numeros) != 11:
            raise forms.ValidationError('Informe 11 números: DDD + número do celular.')

        return f'({numeros[:2]}) {numeros[2:7]}-{numeros[7:]}'

    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        data_perdido = cleaned_data.get('data_perdido')

        if categoria == 'perdido' and not data_perdido:
            self.add_error('data_perdido', 'Informe a data em que o pet desapareceu.')

        return cleaned_data
