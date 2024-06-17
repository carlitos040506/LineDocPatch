from django.shortcuts import render,HttpResponse
# Create your views here.

def login (request):
    return render(request, 'paginas/login.html')

def registro (request):
    return render(request, 'paginas/registro.html')

def iniciar (request):
    return render(request, 'paginas/iniciar.html')

def editar (request):
    return render(request, 'paginas/editar.html')

def perfil (request):
    return render(request, 'paginas/perfil.html')

def bienvenidos (request):
    return render(request, 'paginas/bienvenidos.html')
