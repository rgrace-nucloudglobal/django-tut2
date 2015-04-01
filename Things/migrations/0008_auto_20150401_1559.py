# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0007_auto_20150401_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='enName',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
