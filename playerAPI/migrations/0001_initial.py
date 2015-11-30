# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('position', models.CharField(max_length=100, choices=[(b'QB', b'Quarterback'), (b'RB', b'Runningback'), (b'WR', b'Wide Receiver'), (b'TE', b'Tight End'), (b'DEF', b'Defense')])),
                ('team', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WeekPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week', models.IntegerField()),
                ('points', models.IntegerField()),
                ('player', models.ForeignKey(to='playerAPI.Player')),
            ],
        ),
    ]
