# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerAPI', '0003_auto_20151202_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weekperformance',
            options={'ordering': ['week']},
        ),
    ]
