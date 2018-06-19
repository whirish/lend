# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-23 16:17
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0008_auto_20171126_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=40)),
                ('bio', models.CharField(max_length=300)),
                ('lat', models.DecimalField(decimal_places=8, default=0.0, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, default=0.0, max_digits=11)),
                ('joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.SmallIntegerField(help_text='(In years please!)', validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Item Age'),
        ),
        migrations.AlterField(
            model_name='product',
            name='method',
            field=models.CharField(choices=[('1', 'Delivery'), ('2', 'Pickup'), ('3', 'Delivery & Pickup'), ('4', 'Other Delivery Option')], default='C', max_length=1, verbose_name='Pickup/Delivery Method'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Product Title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Price Per Hour'),
        ),
    ]