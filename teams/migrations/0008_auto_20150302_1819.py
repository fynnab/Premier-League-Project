# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20150301_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='height',
        ),
        migrations.RemoveField(
            model_name='players',
            name='weight',
        ),
    ]
