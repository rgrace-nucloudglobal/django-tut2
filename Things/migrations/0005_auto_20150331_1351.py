# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0004_testname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testname',
            name='myName',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
