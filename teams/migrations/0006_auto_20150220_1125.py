# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20150215_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='clean_sheets',
        ),
        migrations.RemoveField(
            model_name='players',
            name='played',
        ),
        migrations.RemoveField(
            model_name='players',
            name='reds',
        ),
        migrations.RemoveField(
            model_name='players',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='players',
            name='yellows',
        ),
    ]
