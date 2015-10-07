
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


class Perfil_usuario(models.Model):
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

	def __unicode__(self):
		return self.descripcion

class Municipio(models.Model):
	idEstado=models.ForeignKey(Estado)
	clave=models.CharField(max_length=3)
	descripcion=descripcion=models.CharField(max_length=150)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __unicode__(self):
		return self.descripcion

class Oficina(models.Model):
	titulo=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.titulo

class Folios_oficina(models.Model):
	idOficina=models.ForeignKey(Oficina)
	folio_inicial=models.IntegerField()
	folio_final=models.IntegerField()
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.titulo


class Folios_usuario(models.Model):
	idUsuario=models.ForeignKey(User)
	folio_inicial=models.IntegerField()
	folio_final=models.IntegerField()
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User,related_name='usuario_capturo')
	status=models.CharField(max_length=1,choices=status,default='A')

	def __unicode__(self):
		return "%s %s %s" % (self.idUsuario,self.folio_inicial,self.folio_final)

class Usuarios_oficina(models.Model):
	idUsuario=models.ForeignKey(User)
	idOficina=models.ForeignKey(Oficina)
	status=models.CharField(max_length=1,choices=status,default='A')

class Tipo_vehiculo(models.Model):
	descripcion=models.CharField(max_length=50)
	status=models.CharField(max_length=1,choices=status,default='A')	

	def __str__(self):
		return self.descripcion


class Marca(models.Model):
	idTipoVehiculo=models.ForeignKey(Tipo_vehiculo)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __unicode__(self):
		return self.descripcion


class Linea(models.Model):
	idMarca=models.ForeignKey(Marca)
	descripcion=models.CharField(max_length=100)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return self.descripcion


class Propietario(models.Model):
	nombre=models.CharField(max_length=500)
	apellido_paterno=models.CharField(max_length=50)
	apellido_materno=models.CharField(max_length=50,blank=True, null=True)
	sexo=models.ForeignKey(Sexo)
	correo_electronico=models.EmailField(blank=True, null=True)
	idMunicipio=models.ForeignKey(Municipio)
	domicilio=models.TextField(blank=True, null=True)
	telefono=models.CharField(max_length=10,blank=True, null=True)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __unicode__(self):
		return '%s %s %s' % (self.nombre,self.apellido_paterno,self.apellido_materno)


class Vehiculo(models.Model):
	idPropietario=models.ForeignKey(Propietario)
	numero_serie=models.CharField(max_length=17)
	idLinea=models.ForeignKey(Linea)
	color=models.CharField(max_length=50)
	anio=models.ForeignKey(Anio)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __unicode__(self):
		return '%s' % (self.numero_serie)

class Permiso(models.Model):
	folio=models.IntegerField()
	idVehiculo=models.ForeignKey(Vehiculo)
	fecha_capturo=models.DateTimeField(default=timezone.now)
	usuario_capturo=models.ForeignKey(User)
	status=models.CharField(max_length=1,choices=status,default='A')

	def __str__(self):
		return '%s' % (self.folio)



