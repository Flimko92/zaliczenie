# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szkolenia', '0004_auto_20170130_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='document',
            field=models.FileField(upload_to='document/'),
        ),
    ]
