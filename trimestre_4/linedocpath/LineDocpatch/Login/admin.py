from django.contrib import admin
from .models import Usuario, Registrate, Autenticacion, InicioSesion
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Registrate)
admin.site.register(Autenticacion)
admin.site.register(InicioSesion)
