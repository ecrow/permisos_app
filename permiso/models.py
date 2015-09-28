#encoding:utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#opciones
status=(('A','Activo'),('C','Cancelado'))


class Anio(models.Model):
	descripcion=models.CharField(max_length=4)
	status=models.CharField(max_length=1,choices=status,default='A')
	def __str__(self):
		return self.descripcion

class Sexo(models.Model):
	descripcion=models.CharField(max_length=10)
	status=models.CharField(max_length=1,choices=status,default='A')
	def __str__(self):
		return self.descripcion


class Perfil_Usuario(models.Model):
	idUsuario=models.OneToOneField(User)
	apellido_materno=models.CharField(max_length=50)
	

class Vigencia(models.Model):
	descripcion=models.CharField(max_length=50)
	dias=models.IntegerField()
	status=models.CharField(max_length=1,choices=status,default='A')
	def __str__(self):
		return self.descripcion

class Estado(models.Model):
	clave=models.CharField(max_length=2)
	descripcion=models.CharField(max_length=100)
	abreviatura=models.CharField(max_length=50)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.descripcion

class Municipio(models.Model):
	idEstado=models.ForeignKey(Estado)
	clave=models.CharField(max_length=3)
	descripcion=descripcion=models.CharField(max_length=150)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.descripcion

class Oficina(models.Model):
	titulo=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.titulo

class Folios_Oficina(models.Model):
	idOficina=models.ForeignKey(Oficina)
	folio_inicial=models.IntegerField()
	folio_final=models.IntegerField()
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.titulo

class Usuarios_Oficina(models.Model):
	idUsuario=models.ForeignKey(User)
	idOficina=models.ForeignKey(Oficina)
	status=models.CharField(max_length=1,choices=status,default='A')

class Linea(models.Model):
	descripcion=models.CharField(max_length=50)
	status=models.CharField(max_length=1,choices=status,default='A')	

	def __str__(self):
		return self.descripcion


class Marca(models.Model):
	idLinea=models.ForeignKey(Linea)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.descripcion

class Modelo(models.Model):
	idMarca=models.ForeignKey(Marca)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.descripcion


class Propietario(models.Model):
	nombre=models.CharField(max_length=500)
	apellido_paterno=models.CharField(max_length=50)
	apellido_materno=models.CharField(max_length=50)
	sexo=models.ForeignKey(Sexo)
	correo_electronico=models.EmailField(blank=True, null=True)
	idMunicipio=models.ForeignKey(Municipio)
	codigo_postal=models.IntegerField(null=True,blank=True)
	domicilio=models.TextField(blank=True, null=True)
	telefono=models.CharField(max_length=10)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return '%s %s %s' % (self.nombre,self.apellido_paterno,self.apellido_paterno)


class Vehiculo(models.Model):
	numero_serie=models.CharField(max_length=17)
	idModelo=models.ForeignKey(Modelo)
	color=models.CharField(max_length=50)
	anio=models.ForeignKey(Anio)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return '%s' % (self.numero_serie)

class Permiso(models.Model):
	folio=models.IntegerField()
	idVehiculo=models.ForeignKey(Vehiculo)
	idVigencia=models.ForeignKey(Vigencia)
	oficina_capturo=models.ForeignKey(Oficina)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return '%s' % (self.folio)



