from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.PetHelpLoginView.as_view(), name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('sair/', LogoutView.as_view(), name='logout'),
]
