# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='method',
            field=models.CharField(choices=[('C', 'Car')], default='C', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
