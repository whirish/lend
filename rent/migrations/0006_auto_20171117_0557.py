# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 05:57
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20170910_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='posted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
