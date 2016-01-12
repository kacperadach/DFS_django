# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0004_auto_20151206_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekperformance',
            name='player',
            field=models.ForeignKey(related_name='WeekPerformances', to='playerAPI.Player'),
        ),
    ]
