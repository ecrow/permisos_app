# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permiso', '0002_folios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permiso',
            name='oficina_capturo',
        ),
    ]
