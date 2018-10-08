# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-10-07 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='correo',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tiposdeservicio',
            name='imagen',
            field=models.ImageField(upload_to='services'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='imagen',
            field=models.ImageField(upload_to='photos'),
        ),
    ]