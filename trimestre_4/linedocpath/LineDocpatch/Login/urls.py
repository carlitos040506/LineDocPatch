from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='login'),
<<<<<<< HEAD
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
=======
<<<<<<< HEAD
=======
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),
>>>>>>> efd87c475156f5f771a6598395c1db267a9e4ae9
>>>>>>> 0bba83b67e9ee26cebe7fea60f296bbb5b11acf9
]
