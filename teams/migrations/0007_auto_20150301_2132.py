# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20150220_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='club',
            field=models.ForeignKey(to='teams.clubs'),
            preserve_default=True,
        ),
    ]
