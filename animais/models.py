from django.db import models
from django.contrib.auth.models import User

class PublicacaoPet(models.Model):
    CATEGORIAS = [
        ('perdido', 'Pet Perdido'),
        ('encontrado', 'Patinhas Encontradas'),
        ('adocao', 'Adotar um Focinho'),
    ]
    STATUS = [
        ('ativo', 'Ativo'),
        ('resolvido', 'Resolvido'),
    ]
    PORTES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Medio'),
        ('grande', 'Grande'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicacoes')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    foto = models.ImageField(upload_to='animais/')
    nome = models.CharField(max_length=100, blank=True)
    tipo_animal = models.CharField(max_length=80, blank=True, verbose_name='Tipo do animal')
    caracteristicas = models.TextField(blank=True)
    contato = models.CharField(max_length=120, blank=True)
    data_perda = models.DateField(null=True, blank=True, verbose_name='Dia em que foi perdido')
    bairro = models.CharField(max_length=100, blank=True)
    idade = models.CharField(max_length=60, blank=True)
    porte = models.CharField(max_length=20, choices=PORTES, blank=True)
    descricao = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='ativo')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome or self.get_categoria_display()

    @property
    def resolvido(self):
        return self.status == 'resolvido'
