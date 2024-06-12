from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='login'),
    path('', views.registro, name='registro'),
    path('', views.login, name='login'),
    path('', views.perfil, name='login'),
]
