from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.bienvenidos, name='bienvenidos'),
    path('login/', views.login, name='login'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('registro/', views.registro, name='registro'),
    path('editar/', views.editar, name='editar'),
    path('perfil/', views.perfil, name='perfil'),
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'), 
]
