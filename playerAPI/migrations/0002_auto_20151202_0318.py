# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekperformance',
            name='points',
            field=models.IntegerField(blank=True),
        ),
    ]
