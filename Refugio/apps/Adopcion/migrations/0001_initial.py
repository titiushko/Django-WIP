# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
