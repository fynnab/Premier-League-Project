# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20150215_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='logo',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
