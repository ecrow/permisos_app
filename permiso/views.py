#encoding:utf-8
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,Group
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4,landscape
from reportlab.lib.units import inch,cm
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF
import datetime
from .models import *
from .objetos import *

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
		permiso=get_object_or_404(Permiso,pk=folio_pk,idVehiculo=vehiculo)

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
			try:
				busqueda_folio=int(request.GET['busqueda_folio'])
			except ValueError, e:
				return render(request,'permiso/busqueda_folio.html',{'error':'Solo valores númericos como parametro de búsqueda'})				

			lista_permisos=[]
			
			for permiso in Permiso.objects.filter(folio=int(busqueda_folio)):
				permiso_objeto=Permiso_folio()
				
				vigencia=permiso.fecha_capturo+datetime.timedelta(days=30)
				permiso_objeto.idPermiso=permiso.id
				permiso_objeto.folio=permiso.folio
				permiso_objeto.idTipoVehiculo=permiso.idVehiculo.idLinea.idMarca.idTipoVehiculo.id
				permiso_objeto.tipoVehiculo=permiso.idVehiculo.idLinea.idMarca.idTipoVehiculo
				permiso_objeto.idVehiculo=permiso.idVehiculo.id
				permiso_objeto.vehiculo='{} {}'.format(permiso.idVehiculo.idLinea.idMarca,permiso.idVehiculo.idLinea)
				permiso_objeto.serie=permiso.idVehiculo.numero_serie
				permiso_objeto.idPropietario=permiso.idVehiculo.idPropietario.id
				permiso_objeto.propietario=permiso.idVehiculo.idPropietario
				permiso_objeto.expedicion='{}'.format(permiso.fecha_capturo.strftime('%d/%m/%Y'))
				permiso_objeto.vigencia='{}'.format(vigencia.strftime('%d/%m/%Y'))

				lista_permisos.append(permiso_objeto)

			if lista_permisos:
				return render(request,'permiso/busqueda_folio.html',{'lista_permisos':lista_permisos})
			else:
				return render(request,'permiso/mensaje.html',{'msg':'El criterio de búsqueda no encontro resultados'})


	except Exception, e:
		return render(request,'permiso/error.html',{'error':e.message,'e':e})



@login_required
def imprime_folio(request,permiso_pk):
	try:
		permiso=get_object_or_404(Permiso,pk=permiso_pk)
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(str(permiso.folio))

		p = canvas.Canvas(response,pagesize=letter)

		#QR code configuración
		qrw = QrCodeWidget('http://evaluacion.ssm.gob.mx') 
		b = qrw.getBounds()

		w=b[2]-b[0] 
		h=b[3]-b[1] 

		d = Drawing(90,90,transform=[140./w,0,0,140./h,0,0]) 
		d.add(qrw)

		y_pos=0
		for iteracion in range(0,2):
			#Imprime títulos
			p.setFont('Helvetica-Bold',10,leading=None)
			p.drawString(cm*4,cm*(6+y_pos),"LUGAR Y FECHA DE EXPEDICIÓN:")
			p.drawString(cm*4,cm*(4+y_pos),"MARCA")
			p.drawString(cm*8,cm*(4+y_pos),"LÍNEA")
			p.drawString(cm*12,cm*(4+y_pos),"MODELO")
			p.drawString(cm*16,cm*(4+y_pos),"No. DE FOLIO")
			p.drawString(cm*4,cm*(2.5+y_pos),"No. DE SERIE")
			p.drawString(cm*4,cm*(1+y_pos),"COLOR")
			#Imprime datos del permiso
			p.setFont('Helvetica',10,leading=None)
			
			p.drawString(cm*10,cm*(6+y_pos)," CUETZALA GRO. {} ".format(permiso.fecha_capturo.strftime('%d/%m/%Y')))
			p.drawString(cm*4,cm*(4.5+y_pos),"{}".format(permiso.idVehiculo.idLinea.idMarca))
			p.drawString(cm*8,cm*(4.5+y_pos),"{}".format(permiso.idVehiculo.idLinea))
			p.drawString(cm*12,cm*(4.5+y_pos),"{}".format(permiso.idVehiculo.anio))
			p.drawString(cm*16,cm*(4.5+y_pos),"{}".format(permiso.folio))
			p.drawString(cm*4,cm*(3+y_pos),"{}".format(permiso.idVehiculo.numero_serie))
			p.drawString(cm*4,cm*(1.5+y_pos),"%s" % permiso.idVehiculo.color)

			#renderiza QR Code
			renderPDF.draw(d, p, cm*14, cm*(7+y_pos))

			y_pos+=14


		p.showPage()
		p.save()

		return response
	except Exception, e:
		return render(request,'permiso/error.html',{'error':e.message})

@login_required
def vehiculo(request,vehiculo_pk):
	try:
		vehiculo=get_object_or_404(Vehiculo,pk=vehiculo_pk)
		permisos_vehiculo=[]

		for permiso in vehiculo.permiso_set.all():
				permiso_objeto=Permiso_folio()
				
				vigencia=permiso.fecha_capturo+datetime.timedelta(days=30)
				permiso_objeto.idPermiso=permiso.id
				permiso_objeto.folio=permiso.folio
				permiso_objeto.idVehiculo=permiso.idVehiculo.id
				permiso_objeto.tipoVehiculo=permiso.idVehiculo.idLinea.idMarca.idTipoVehiculo
				permiso_objeto.vehiculo='{} {}'.format(permiso.idVehiculo.idLinea.idMarca,permiso.idVehiculo.idLinea)
				permiso_objeto.serie=permiso.idVehiculo.numero_serie
				permiso_objeto.idPropietario=permiso.idVehiculo.idPropietario.id
				permiso_objeto.propietario=permiso.idVehiculo.idPropietario
				permiso_objeto.expedicion='{}'.format(permiso.fecha_capturo.strftime('%d/%m/%Y'))
				permiso_objeto.vigencia='{}'.format(vigencia.strftime('%d/%m/%Y'))
				permisos_vehiculo.append(permiso_objeto)

		return render(request,'permiso/vehiculo.html',{'vehiculo':vehiculo,'permisos_vehiculo':permisos_vehiculo})

	except Exception, e:
		return render(request,'permiso/vehiculo.html',{'error',e.message})	


@login_required
def propietario(request,propietario_pk):
	try:
		propietario=get_object_or_404(Propietario,pk=propietario_pk)
		vehiculos_propietario=propietario.vehiculo_set.all()
		
		return render(request,'permiso/propietario.html',{'propietario':propietario,'vehiculos_propietario':vehiculos_propietario})
	except Exception, e:
		return render(request,'permiso/propietario.html',{'error',e.message})

	

@login_required
def usuarios(request):
	try:
		usuarios=User.objects.all()
		return render(request,'permiso/usuarios.html',{'usuarios':usuarios})
	except Exception, e:
		return render(request,'permiso/error.html',{'error',e.message})




	

		