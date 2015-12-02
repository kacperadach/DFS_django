# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0002_auto_20151202_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekperformance',
            name='week',
            field=models.IntegerField(blank=True),
        ),
    ]
