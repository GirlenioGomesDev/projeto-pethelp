from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets-perdidos/', views.lista_categoria, {'categoria': 'perdido'}, name='pets_perdidos'),
    path('patinhas-encontradas/', views.lista_categoria, {'categoria': 'encontrado'}, name='patinhas_encontradas'),
    path('adotar-um-focinho/', views.lista_categoria, {'categoria': 'adocao'}, name='adotar_focinho'),
    path('publicacao/<int:pk>/', views.detalhe_publicacao, name='detalhe_publicacao'),
    path('cadastrar/', views.cadastrar_publicacao, name='cadastrar_publicacao'),
    path('minhas-publicacoes/', views.minhas_publicacoes, name='minhas_publicacoes'),
    path('editar/<int:pk>/', views.editar_publicacao, name='editar_publicacao'),
    path('status/<int:pk>/', views.alternar_status_publicacao, name='alternar_status_publicacao'),
    path('apagar/<int:pk>/', views.apagar_publicacao, name='apagar_publicacao'),
    path('login/', views.PetHelpLoginView.as_view(), name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('sair/', LogoutView.as_view(), name='logout'),
]
