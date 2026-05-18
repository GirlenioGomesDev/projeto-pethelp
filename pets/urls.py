from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.galeria, name='galeria_pets'),
    path('pets-perdidos/', views.lista_categoria, {'categoria': 'perdido'}, name='pets_perdidos'),
    path('patinhas-encontradas/', views.lista_categoria, {'categoria': 'encontrado'}, name='patinhas_encontradas'),
    path('adotar-focinho/', views.lista_categoria, {'categoria': 'adocao'}, name='adotar_focinho'),
    path('pet/<int:pk>/', views.detalhe_pet, name='detalhe_pet'),
    path('cadastrar-pet/', views.cadastrar_pet, name='cadastrar_pet'),
    path('minhas-publicacoes/', views.minhas_publicacoes, name='minhas_publicacoes'),
    path('pet/<int:pk>/editar/', views.editar_pet, name='editar_pet'),
    path('pet/<int:pk>/excluir/', views.excluir_pet, name='excluir_pet'),
]
