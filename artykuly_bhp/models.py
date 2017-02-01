# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from pracownicy.models import Worker

class produkty(models.Model):

    name = models.CharField(max_length=40)
    count = models.PositiveIntegerField()
    exp_date = models.DateField()

    def __unicode__(self):
        return u"%s / %s" % (self.name, self.exp_date)

class przydzial(models.Model):

    who = models.ForeignKey(Worker)
    what = models.ManyToManyField(produkty)
    when = models.DateField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return u"%s" % (self.when)
