# coding: utf-8

from __future__ import unicode_literals

from django.db import models

class documentation(models.Model):

    name = models.CharField(max_length=20)
    document = models.FileField(upload_to='document/')

    def __unicode__(self):
        return u"%s" % (self.name)

class instruction(models.Model):

    name = models.CharField(max_length=30)
    duration = models.DurationField()
    description = models.TextField(max_length=500)
    documentation = models.ManyToManyField(documentation, blank=True)

    def __unicode__(self):
        return u"%s" % (self.name)
