# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('szkolenia', '0002_auto_20170130_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='document',
            field=models.FileField(storage='/document', upload_to='/document'),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='documentation',
            field=models.ManyToManyField(blank=True, to='szkolenia.documentation'),
        ),
    ]
