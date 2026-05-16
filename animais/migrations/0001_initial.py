# Generated manually for PetHelp
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicacaoPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('perdido', 'Pet Perdido'), ('encontrado', 'Patinhas Encontradas'), ('adocao', 'Adotar um Focinho')], max_length=20)),
                ('foto', models.ImageField(upload_to='animais/')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('caracteristicas', models.TextField(blank=True)),
                ('contato', models.CharField(blank=True, max_length=120)),
                ('data_perda', models.DateField(blank=True, null=True, verbose_name='Dia em que foi perdido')),
                ('bairro', models.CharField(blank=True, max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicacoes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
    ]
