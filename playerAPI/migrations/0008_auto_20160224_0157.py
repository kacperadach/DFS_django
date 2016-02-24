# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0007_player_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fppg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='opp',
            field=models.CharField(default=b'N/A', max_length=100),
        ),
    ]
