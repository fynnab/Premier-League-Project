# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('position', models.CharField(default=b'GK', max_length=64, choices=[(b'GK', b'Goalkeeper'), (b'DEF', b'Defender'), (b'MID', b'Midfielder'), (b'FWD', b'Forward')])),
                ('born', models.DateField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('nationality', models.CharField(max_length=64)),
                ('played', models.IntegerField()),
                ('clean_sheets', models.IntegerField()),
                ('scored', models.IntegerField()),
                ('yellows', models.IntegerField()),
                ('reds', models.IntegerField()),
                ('club', models.OneToOneField(related_name='team', to='teams.clubs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
