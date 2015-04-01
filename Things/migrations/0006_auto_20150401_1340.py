# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0005_auto_20150331_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='color',
            field=models.ForeignKey(related_name='+', to='Things.Color'),
            preserve_default=True,
        ),
    ]
