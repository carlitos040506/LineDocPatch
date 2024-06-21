from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistrateForm,UsuarioForm
from .models import Usuario
# Create your views here.

def login (request):
    return render(request, 'paginas/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenidos')  # Redirige después de guardar
    else:
        form = RegistrateForm()
    return render(request, 'paginas/registro.html', {'form': form})

def editar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'paginas/editar.html', {'form': form})

def iniciar (request):
    return render(request, 'paginas/iniciar.html')

def editar (request):
    return render(request, 'paginas/editar.html')

def perfil (request):
    return render(request, 'paginas/perfil.html')

def bienvenidos (request):
    return render(request, 'paginas/bienvenidos.html')

@login_required
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('bienvenidos')  # Redirige a la página de inicio o de confirmación después de eliminar

    return render(request, 'paginas/eliminar_confirm.html', {'usuario': usuario})
