# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('szkolenia', '0001_initial'),
        ('pracownicy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_instruction', models.DateField()),
                ('next_instruction', models.DateField()),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkolenia.instruction')),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='course',
            field=models.ManyToManyField(to='pracownicy.Course'),
        ),
    ]