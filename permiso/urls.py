from django.conf.urls import url
from . import views

urlpatterns = [
	
    url(r'^registro/propietario/$', views.guarda_datos_propietario,name="vregistro_propietario"),
    url(r'^registro/propietario/(?P<propietario_pk>\d+)/vehiculo/$', views.guarda_datos_vehiculo,name="vregistro_vehiculo"),
    url(r'^registro/propietario/(?P<propietario_pk>\d+)/vehiculo/(?P<vehiculo_pk>\d+)/folio/$', views.guarda_datos_folio,name="vregistro_folio"),
    url(r'^registro/propietario/(?P<propietario_pk>\d+)/vehiculo/(?P<vehiculo_pk>\d+)/folio/(?P<folio_pk>\d+)/$', views.permiso_folio,name="vpermiso_folio"),

    url(r'^rango/folios/$',views.rango_folios,name="rango_folios"),
    url(r'^rango/folios/usuario/(?P<usuario_pk>\d+)/$',views.folios_usuario,name="folios_usuario"),
    url(r'^usuario/nuevo/$',views.usuario_nuevo,name="usuario_nuevo"),
    url(r'^busqueda/folio/$',views.busqueda_folio,name="busqueda_folio"),
    url(r'^busqueda/propietario/$',views.busqueda_propietario,name="busqueda_propietario"),
    url(r'^busqueda/general/$',views.busqueda_general,name="busqueda_general"),
    url(r'^imprime/permiso/(?P<permiso_pk>\d+)/$',views.imprime_folio, name="imprime_folio"),
 	url(r'^datos/vehiculo/(?P<vehiculo_pk>\d+)/$',views.vehiculo, name="vehiculo"),
    url(r'^datos/propietario/(?P<propietario_pk>\d+)/$',views.propietario, name="propietario"),
    url(r'^usuarios/$',views.usuarios, name="usuarios"),
]
