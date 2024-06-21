from django.db import models

# Create your models here.

# Modelo para los usuarios
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(max_length=254, unique=True)
    nombre_de_usuario = models.CharField(max_length=45, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=10, choices=[('Mujer', 'Mujer'), ('Hombre', 'Hombre'), ('Otro', 'Otro')], blank=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

# Modelo para el registro de usuarios
class Registrate(models.Model):
    idRegistrate = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    fechadeNacimiento = models.DateField()
    correoElectronicooCelular = models.CharField(max_length=45, unique=True)
    nombredeusuario = models.CharField(max_length=45, unique=True)
    contrasena = models.CharField(max_length=45)

    def __str__(self):
        return self.nombredeusuario

# Modelo para la autenticación
class Autenticacion(models.Model):
    idAutenticacion = models.AutoField(primary_key=True)
    correoElectronicooCelular = models.CharField(max_length=45, unique=True)
    codigo = models.CharField(max_length=45, unique=True, editable=False)
    nuevaContrasena = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return f'Autenticacion {self.idAutenticacion}'

# Modelo para el inicio de sesión
class InicioSesion(models.Model):
    idInicioSesion = models.AutoField(primary_key=True)
    nombredeUsuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    olvideContrasena = models.CharField(max_length=45, null=True, blank=True, unique=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    registrate = models.ForeignKey(Registrate, on_delete=models.CASCADE)
    autenticacion = models.ForeignKey(Autenticacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'Inicio de sesión {self.idInicioSesion}'
