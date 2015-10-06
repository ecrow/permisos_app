# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('permiso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folios_usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folio_inicial', models.IntegerField()),
                ('folio_final', models.IntegerField()),
                ('fecha_capturo', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')])),
                ('idUsuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('usuario_capturo', models.ForeignKey(related_name='usuario_capturo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
