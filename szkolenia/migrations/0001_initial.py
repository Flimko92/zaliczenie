# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('document', models.FileField(upload_to='document/')),
            ],
        ),
        migrations.CreateModel(
            name='instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('duration', models.DurationField()),
                ('description', models.TextField(max_length=500)),
                ('documentation', models.ManyToManyField(blank=True, to='szkolenia.documentation')),
            ],
        ),
    ]