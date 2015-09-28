# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permiso', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permiso',
            name='status',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'C', b'Cancelado')]),
        ),
    ]
