# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 18:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pracownicy', '0003_auto_20170131_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]