# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enName', models.CharField(help_text=b'enter a value', max_length=200, verbose_name=b'Name')),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enName', models.CharField(max_length=200, verbose_name=b'Name')),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enName', models.CharField(max_length=200, verbose_name=b'Name')),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('color', models.ForeignKey(to='Things.Color')),
                ('shape', models.ForeignKey(to='Things.Shape')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
