from django.urls import path,views

urlpatterns = [
    path('', views.login, name='login'),
]
