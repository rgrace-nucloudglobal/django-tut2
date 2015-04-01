# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Things', '0003_auto_20150316_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('myName', models.CharField(max_length=100, verbose_name=b'MyName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
