# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0006_auto_20150401_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='color',
            field=models.ForeignKey(to='Things.Color'),
            preserve_default=True,
        ),
    ]
