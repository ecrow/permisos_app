#encoding:utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#clases de catálogos generales
from .models import Anio,Sexo,Vigencia,Estado,Municipio,Oficina,Usuarios_oficina,Linea,Marca,Tipo_vehiculo,Folios_usuario
#clases de produccion
from .models import Propietario,Vehiculo,Permiso
#clase para extender los datos de usuario
from .models import Perfil_usuario



class PerfilUsuarioInline(admin.StackedInline):
    model = Perfil_usuario
    can_delete = False
    verbose_name_plural = 'perfil'

class UserAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline, )


class lineaInline(admin.StackedInline):
	model=Linea

class marcaInline(admin.StackedInline):
	model=Marca


class tipoVehiculoAdmin(admin.ModelAdmin):
	inlines=[marcaInline, ]


#registro de catálogos en admin

admin.site.register(Tipo_vehiculo, tipoVehiculoAdmin)

admin.site.register(Anio)
admin.site.register(Sexo)
admin.site.register(Vigencia)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Oficina)
admin.site.register(Usuarios_oficina)
admin.site.register(Marca)
admin.site.register(Linea)
admin.site.register(Folios_usuario)

#registro de tablas de producción en admin
admin.site.register(Propietario)
admin.site.register(Vehiculo)
admin.site.register(Permiso)

#admin de usuario
admin.site.unregister(User)
admin.site.register(User, UserAdmin)