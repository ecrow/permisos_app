from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User

from permiso.models import *


@login_required
def index(request):
	return render(request,'index.html')

@login_required
def catalogo_sexo(request):
	lista_sexo = []
	for sexo in Sexo.objects.filter(status='A').order_by('id'):
		lista_sexo.append({'idsexo_id': sexo.id,'descripcion': sexo.descripcion})
	return JsonResponse(lista_sexo,safe=False)


@login_required
def catalogo_estado(request):
	lista_estado = []
	for estado in Estado.objects.filter(status='A').order_by('id'):
		lista_estado.append({'idestado_id': estado.id,'descripcion': estado.descripcion})
	return JsonResponse(lista_estado,safe=False)


@login_required
def catalogo_municipio(request):
	lista_municipio = []
	for municipio in Municipio.objects.filter(status='A').order_by('id'):
		lista_municipio.append({'idmunicipio_id': municipio.id,'idestado_id':municipio.idEstado.id,'descripcion': municipio.clave+'-'+municipio.descripcion})
	return JsonResponse(lista_municipio,safe=False)


@login_required
def catalogo_tipo_vehiculo(request):
	lista_tipo_vehiculo = []
	for tipo in Tipo_vehiculo.objects.filter(status='A').order_by('id'):
		lista_tipo_vehiculo.append({'idtipo_vehiculo_id': tipo.id,'descripcion': tipo.descripcion})
	return JsonResponse(lista_tipo_vehiculo,safe=False)


@login_required
def catalogo_marca_vehiculo(request):
	lista_marca_vehiculo = []
	for marca in Marca.objects.filter(status='A').order_by('id'):
		lista_marca_vehiculo.append({'idmarca_vehiculo_id': marca.id,'idtipo_vehiculo_id': marca.idTipoVehiculo.id,'descripcion': marca.descripcion})
	return JsonResponse(lista_marca_vehiculo,safe=False)


@login_required
def catalogo_linea_vehiculo(request):
	lista_linea_vehiculo = []
	for linea in Linea.objects.filter(status='A').order_by('id'):
		lista_linea_vehiculo.append({'idlinea_vehiculo_id': linea.id,'idmarca_vehiculo_id': linea.idMarca.id,'descripcion': linea.descripcion})
	return JsonResponse(lista_linea_vehiculo,safe=False)


@login_required
def catalogo_modelo_vehiculo(request):
	lista_modelo_vehiculo = []
	for modelo in Anio.objects.filter(status='A').order_by('id'):
		lista_modelo_vehiculo.append({'idmodelo_vehiculo_id': modelo.id,'descripcion': modelo.descripcion})
	return JsonResponse(lista_modelo_vehiculo,safe=False)

@login_required
def catalogo_usuarios(request):
	lista_usuarios = []
	for usuario in User.objects.all():
		lista_usuarios.append({'idusuario_id': usuario.id,'descripcion': usuario.first_name+' '+usuario.last_name})
	return JsonResponse(lista_usuarios,safe=False)


@login_required
def catalogo_folios(request):
	lista_folios_usuario = []
	folios_registrados = [int(folio_utilizado.folio) for folio_utilizado in Permiso.objects.filter(status='A')]
	lista_folios=[numero for folio in Folios_usuario.objects.filter(idUsuario=request.user,status='A') for numero in range(folio.folio_inicial,folio.folio_final+1) ]
	for folio_lista in lista_folios:
		if folio_lista not in folios_registrados:
			lista_folios_usuario.append({'idfolio_id': folio_lista,'folio': str(folio_lista)})
	return JsonResponse(lista_folios_usuario,safe=False)


	
	



	