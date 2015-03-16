# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20150302_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='established',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
    ]
