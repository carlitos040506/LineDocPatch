from django.shortcuts import render,HttpResponse
# Create your views here.

def inicio (request):
    return render(request, 'paginas/login.html')

def registro (request):
    return render(request, 'paginas/registro.html')

def login (request):
    return render(request, 'paginas/index.html')

def perfil (request):
    return render(request, 'paginas/perfil.html')
