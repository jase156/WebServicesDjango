# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(default='', max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('codigo', models.CharField(default='', max_length=5, unique=True)),
                ('cupos', models.SmallIntegerField(default=0)),
                ('matriculados', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAlumno', models.CharField(max_length=12)),
                ('idMateria', models.CharField(max_length=5)),
            ],
        ),
    ]
