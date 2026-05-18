from django.conf import settings
from django.db import models


class Pet(models.Model):
    # Valores curtos ficam no banco; labels amigaveis aparecem nos forms, cards e admin.
    CATEGORIAS = [
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('adocao', 'Adoção'),
    ]
    PORTES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]

    nome = models.CharField('nome do pet', max_length=120)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    foto = models.ImageField(upload_to='pets/')
    raca = models.CharField('raça', max_length=100, blank=True)
    idade = models.CharField(max_length=60, blank=True)
    porte = models.CharField(max_length=20, choices=PORTES)
    bairro = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    data_perdido = models.DateField('data em que desapareceu', null=True, blank=True)
    caracteristicas = models.TextField('características específicas')
    telefone = models.CharField('número para contato', max_length=30)
    descricao = models.TextField('descrição opcional', blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'pet'
        verbose_name_plural = 'pets'

    def __str__(self):
        return f'{self.nome} - {self.get_categoria_display()}'
