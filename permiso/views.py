from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,Group
import datetime
from .models import *

@login_required
def registro(request):
	return render(request,'permiso/registro_propietario.html',{})

@login_required
def guarda_datos_propietario(request):
	if request.method=='POST':
		if 'submit_propietario' in request.POST:
			try:
				nombre=request.POST['name_propietario']
				apellido_paterno=request.POST['lname_propietario']
				apellido_materno=request.POST['tname_propietario']
				sexo=request.POST['sexo_propietario']
				correo_electronico=request.POST['email_propietario']
				telefono=request.POST['telefono_propietario']
				idMunicipio=request.POST['municipio_propietario']
				domicilio=request.POST['direccion_propietario']
				usuario_capturo=request.user
				fecha_capturo=timezone.now()

				sexoObject=Sexo.objects.get(pk=sexo,status='A')
				municipioObject=Municipio.objects.get(pk=idMunicipio,status='A')

				nuevo_propietario=Propietario.objects.create(
					nombre=nombre.upper(),
					apellido_paterno=apellido_paterno.upper(),
					apellido_materno=apellido_materno.upper(),
					sexo=sexoObject,
					correo_electronico=correo_electronico.lower(),
					telefono=telefono,
					idMunicipio=municipioObject,
					domicilio=domicilio.upper(),
					usuario_capturo=usuario_capturo,
					fecha_capturo=fecha_capturo
					)
				
				return HttpResponseRedirect(reverse('vregistro_vehiculo', kwargs={'propietario_pk':nuevo_propietario.id}))

			except Exception, e:
				render(request,'permiso/registro_propietario.html',{'error':e.message})
	return render(request,'permiso/registro_propietario.html',{})

@login_required
def guarda_datos_vehiculo(request,propietario_pk):
	try:
		propietario=get_object_or_404(Propietario,pk=propietario_pk)
		if request.method=='POST':
			if 'submit_vehiculo' in request.POST:
				try:
					numero_serie=request.POST['serie_vehiculo']
					idLinea=request.POST['linea_vehiculo']
					color=request.POST['color_vehiculo']
					anio=request.POST['modelo_vehiculo']
					fecha_capturo=timezone.now()
					usuario_capturo=request.user
					
					lineaObject=Linea.objects.get(pk=idLinea,status='A')
					anioObject=Anio.objects.get(pk=anio,status='A')

					nuevo_vehiculo=Vehiculo.objects.create(
							idPropietario=propietario,
							numero_serie=numero_serie.upper(),
							idLinea=lineaObject,
							color=color.upper(),
							anio=anioObject,
							usuario_capturo=usuario_capturo,
							fecha_capturo=fecha_capturo
							)

					return HttpResponseRedirect(reverse('vregistro_folio', kwargs={'propietario_pk':propietario.id,
						'vehiculo_pk':nuevo_vehiculo.id}))

				except Exception, e:
					return render(request,'permiso/registro_vehiculo.html',{'error':e.message})
		return render(request,'permiso/registro_vehiculo.html',{'propietario':propietario})	

	except Exception, e:
		return render(request,'permiso/registro_vehiculo.html',{'error':e.message})


@login_required
def guarda_datos_folio(request,propietario_pk,vehiculo_pk):
	try:
		propietario=get_object_or_404(Propietario,pk=propietario_pk)
		vehiculo=get_object_or_404(Vehiculo,pk=vehiculo_pk,idPropietario=propietario)

		if request.method=='POST':
			if 'submit_folio' in request.POST:
				try:
					folio_permiso=request.POST['folio_permiso']
					fecha_capturo=timezone.now()
					usuario_capturo=request.user

					nuevo_permiso=Permiso.objects.create(
						folio=int(folio_permiso),
						idVehiculo=vehiculo,
						usuario_capturo=usuario_capturo,
						fecha_capturo=fecha_capturo
						)
					return HttpResponseRedirect(reverse('vpermiso_folio', kwargs={'propietario_pk':propietario.id,
						'vehiculo_pk':vehiculo.id,'folio_pk':nuevo_permiso.id}))

				except Exception, e:
					return render(request,'permiso/registro_folio.html',{'propietario':propietario,'vehiculo':vehiculo})
			
		return render(request,'permiso/registro_folio.html',{'propietario':propietario,'vehiculo':vehiculo})
	except Exception, e:
		return render(request,'permiso/registro_folio.html',{'error':e.message})

@login_required
def permiso_folio(request,propietario_pk,vehiculo_pk,folio_pk):
	try:
		propietario=get_object_or_404(Propietario,pk=propietario_pk)
		vehiculo=get_object_or_404(Vehiculo,pk=vehiculo_pk,idPropietario=propietario)
		permiso=get_object_or_404(Permiso,idVehiculo=vehiculo)

		vigencia=permiso.fecha_capturo+datetime.timedelta(days=30)

		return render(request,'permiso/permiso_folio.html',{'propietario':propietario,'vehiculo':vehiculo,'permiso':permiso,
			'vigencia':vigencia})

	except Exception, e:
		return render(request,'permiso/permiso_folio.html',{'error':e.message})



@login_required
def rango_folios(request):
	try:
		if request.method=='POST':
			if 'submit_rango' in request.POST:
				try:
					idUsuario=request.POST['usuario_rango']
					folio_inicial=request.POST['folioini_rango']
					folio_final=request.POST['foliofin_rango']
					fecha_capturo=timezone.now()
					usuario_capturo=request.user

					if int(folio_final)<int(folio_inicial):
						raise Exception('El folio inicial debe ser menor o igual que el folio final')

						
					usuarioObject=User.objects.get(pk=idUsuario)
					if any(int(folio_inicial) <= folio_usuario.folio_inicial <= int(folio_final) for folio_usuario in Folios_usuario.objects.filter(idUsuario=usuarioObject,status='A')):
						raise Exception('El folio inicial ya se encuentra en un rango asignado')	
					elif any(int(folio_inicial) <= folio_usuario.folio_final <= int(folio_final) for folio_usuario in Folios_usuario.objects.filter(idUsuario=usuarioObject,status='A')):
						raise Exception('El folio final ya se encuentra en un rango asignado')
					

					rango_nuevo=Folios_usuario.objects.create(
						idUsuario=usuarioObject,
						folio_inicial=folio_inicial,
						folio_final=folio_final,
						usuario_capturo=usuario_capturo,
						fecha_capturo=fecha_capturo
						)
					return render(request,'permiso/rango_folios.html',{})
				except Exception, e:
					return render(request,'permiso/rango_folios.html',{'error':e.message})		
		return render(request,'permiso/rango_folios.html',{})
	except Exception, e:
		return render(request,'permiso/rango_folios.html',{'error':e.message})	

@login_required
def folios_usuario(request,usuario_pk):
	lista_folios_usuario = []
	for folio_usuario in Folios_usuario.objects.filter(idUsuario=usuario_pk,status='A'):
		lista_folios_usuario.append({'folio_ini': folio_usuario.folio_inicial,'folio_fin': folio_usuario.folio_final})
	return JsonResponse(lista_folios_usuario,safe=False)


@login_required
def usuario_nuevo(request):
	try:
		if request.method=='POST':
			if 'submit_nuevo_usuario' in request.POST:
				try:
					user_name=request.POST['username_usuario']
					user_pwd=request.POST['pwd_usuario']
					user_nombre=request.POST['nombre_usuario']
					user_apaterno=request.POST['apaterno_usuario']
					user_amaterno=request.POST['amaterno_usuario']
					user_email=request.POST['email_usuario']

					user = User.objects.create_user(
						username=user_name,
						email=user_email if user_email else None,
						password=user_pwd
						)

					user_is_licencias=request.POST['usuario_grupo_licencias'] if 'usuario_grupo_licencias' in request.POST else False

					grupoLicencias = Group.objects.get(name='Licencias') 

					if 'usuario_grupo_coordinador' in request.POST:
						grupoCoordinadores = Group.objects.get(name='Coordinadores') 
						user.groups.add(grupoCoordinadores)

					if 'usuario_grupo_licencias' in request.POST:
						grupoLicencias = Group.objects.get(name='Licencias') 
						user.groups.add(grupoLicencias)

					if 'usuario_admin' in request.POST: 
						user.is_superuser=True
					

					user.first_name=user_nombre
					user.last_name=user_apaterno
					user.save()

					Perfil_usuario(idUsuario=user,apellido_materno=user_amaterno).save()

					return render(request,'permiso/usuario_nuevo.html',{'msg':'Usuario creado con exito'})

				except Exception, e:
					return render(request,'permiso/usuario_nuevo.html',{'error':e.message})


	except Exception, e:
		return render(request,'permiso/usuario_nuevo.html',{'error':e.message})
	
	return render(request,'permiso/usuario_nuevo.html',{})


@login_required
def busqueda_folio(request):
	try:
		if request.method=='GET':
			busqueda_folio=request.GET['busqueda_folio']
			folio=get_object_or_404(Permiso,folio=int(busqueda_folio))
			return render(request,'permiso/busqueda_folio.html',{'error':e.message})

	except Exception, e:
		return render(request,'permiso/busqueda_folio.html',{'error':e.message})



	

		