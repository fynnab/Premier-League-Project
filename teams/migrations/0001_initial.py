# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clubs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('nickname', models.CharField(max_length=64)),
                ('logo', models.ImageField(upload_to=b'')),
                ('manager', models.CharField(max_length=128)),
                ('established', models.IntegerField()),
                ('stadium', models.CharField(max_length=64)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
