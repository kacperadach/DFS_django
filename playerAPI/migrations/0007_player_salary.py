# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0006_player_total_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
