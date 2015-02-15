# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20150215_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 2, 15, 11, 14, 25, 999000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='players',
            name='height',
            field=models.DecimalField(max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
