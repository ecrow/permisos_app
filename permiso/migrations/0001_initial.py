# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=4)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Folios_oficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folio_inicial', models.IntegerField()),
                ('folio_final', models.IntegerField()),
                ('fecha_capturo', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave', models.CharField(max_length=3)),
                ('descripcion', models.CharField(max_length=150)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
                ('idEstado', models.ForeignKey(to='permiso.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('idUsuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folio', models.IntegerField()),
                ('fecha_capturo', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50, null=True, blank=True)),
                ('correo_electronico', models.EmailField(max_length=254, null=True, blank=True)),
                ('domicilio', models.TextField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=10, null=True, blank=True)),
                ('fecha_capturo', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
                ('idMunicipio', models.ForeignKey(to='permiso.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=10)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios_oficina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
                ('idOficina', models.ForeignKey(to='permiso.Oficina')),
                ('idUsuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_serie', models.CharField(max_length=17)),
                ('color', models.CharField(max_length=50)),
                ('fecha_capturo', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
                ('anio', models.ForeignKey(to='permiso.Anio')),
                ('idLinea', models.ForeignKey(to='permiso.Linea')),
                ('idPropietario', models.ForeignKey(to='permiso.Propietario')),
                ('usuario_capturo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vigencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('dias', models.IntegerField()),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
            ],
        ),
        migrations.AddField(
            model_name='propietario',
            name='sexo',
            field=models.ForeignKey(to='permiso.Sexo'),
        ),
        migrations.AddField(
            model_name='propietario',
            name='usuario_capturo',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='permiso',
            name='idVehiculo',
            field=models.ForeignKey(to='permiso.Vehiculo'),
        ),
        migrations.AddField(
            model_name='permiso',
            name='oficina_capturo',
            field=models.ForeignKey(to='permiso.Oficina'),
        ),
        migrations.AddField(
            model_name='permiso',
            name='usuario_capturo',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='marca',
            name='idTipoVehiculo',
            field=models.ForeignKey(to='permiso.Tipo_vehiculo'),
        ),
        migrations.AddField(
            model_name='linea',
            name='idMarca',
            field=models.ForeignKey(to='permiso.Marca'),
        ),
        migrations.AddField(
            model_name='folios_oficina',
            name='idOficina',
            field=models.ForeignKey(to='permiso.Oficina'),
        ),
        migrations.AddField(
            model_name='folios_oficina',
            name='usuario_capturo',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
