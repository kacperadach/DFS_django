# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0005_auto_20160112_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]
