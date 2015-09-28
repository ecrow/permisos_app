#encoding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#clases de catálogos generales
from .models import Anio,Sexo,Vigencia,Estado,Municipio,Oficina,Folios_Oficina,Usuarios_Oficina,Linea,Marca,Modelo
#clases de produccion
from .models import Propietario,Vehiculo,Permiso
#clase para extender los datos de usuario
from .models import Perfil_Usuario


class PerfilUsuarioInline(admin.StackedInline):
    model = Perfil_Usuario
    can_delete = False
    verbose_name_plural = 'perfil'

class UserAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline, )


#registro de catálogos en admin

admin.site.register(Anio)
admin.site.register(Sexo)
admin.site.register(Vigencia)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Oficina)
admin.site.register(Folios_Oficina)
admin.site.register(Usuarios_Oficina)
admin.site.register(Linea)
admin.site.register(Marca)
admin.site.register(Modelo)

#registro de tablas de producción en admin
admin.site.register(Propietario)
admin.site.register(Vehiculo)
admin.site.register(Permiso)

#admin de usuario
admin.site.unregister(User)
admin.site.register(User, UserAdmin)