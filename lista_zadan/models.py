# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from artykuly_bhp.models import produkty
from pracownicy.models import Worker

class alert(models.Model):

    braki_magazynowe = models.ManyToManyField(produkty)
    nadchodzace_szkolenia = models.ManyToManyField(Worker)
