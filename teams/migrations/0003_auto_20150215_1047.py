# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clubs',
            old_name='current',
            new_name='active',
        ),
        migrations.AddField(
            model_name='players',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='players',
            name='height',
            field=models.DecimalField(max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
    ]
