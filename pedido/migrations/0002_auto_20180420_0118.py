# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='metodo',
            field=models.CharField(blank=True, choices=[('1', 'Dinheiro'), ('2', 'C. Debito'), ('3', 'C. Credito')], max_length=1, null=True),
        ),
    ]