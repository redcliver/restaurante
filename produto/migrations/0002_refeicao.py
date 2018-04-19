# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='refeicao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
