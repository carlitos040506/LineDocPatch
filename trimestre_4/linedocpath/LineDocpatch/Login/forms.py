

from django import forms
from .models import Usuario, Registrate, Autenticacion, InicioSesion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre', 'apellido', 'email', 'telefono', 'genero',
            'fecha_de_nacimiento', 'descripcion'
        ]

class RegistrateForm(forms.ModelForm):
    class Meta:
        model = Registrate
        fields = [
            'nombres', 'apellidos', 'fechadeNacimiento', 
            'correoElectronicoCelular', 'nombredeusuario', 'contrasena'
        ]

class AutenticacionForm(forms.ModelForm):
    class Meta:
        model = Autenticacion
        fields = ['correoElectronicoCelular', 'codigo', 'nuevaContrasena']

class InicioSesionForm(forms.ModelForm):
    class Meta:
        model = InicioSesion
        fields = ['nombredeUsuario', 'contrasena']
