# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0008_auto_20150401_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='description',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shape',
            name='description',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thing',
            name='enName',
            field=models.CharField(max_length=210),
            preserve_default=True,
        ),
    ]
