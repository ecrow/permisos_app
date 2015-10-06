"""permisos_sitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^permiso/',include('permiso.urls')),
    url(r'^admin/', include(admin.site.urls)),	
    url('^', include('django.contrib.auth.urls')),
    url(r'^logout_login/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^catalogo/sexo',views.catalogo_sexo),
    url(r'^catalogo/estado',views.catalogo_estado),
    url(r'^catalogo/municipio',views.catalogo_municipio),
    url(r'^catalogo/tipo_vehiculo',views.catalogo_tipo_vehiculo),
    url(r'^catalogo/marca_vehiculo',views.catalogo_marca_vehiculo),
    url(r'^catalogo/linea_vehiculo',views.catalogo_linea_vehiculo),
    url(r'^catalogo/modelo_vehiculo',views.catalogo_modelo_vehiculo),
    url(r'^catalogo/usuarios/$',views.catalogo_usuarios),
    url(r'^catalogo/folios/$',views.catalogo_folios,name="folios"),
    

]

urlpatterns +=staticfiles_urlpatterns()