from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='login'),
    path('registro/', views.registro, name='registro'),
    path('index/', views.login, name='index'),
    path('perfil/', views.perfil, name='perfil'),
]
