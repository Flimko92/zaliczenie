# coding: utf-8
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from szkolenia.models import instruction

class Course(models.Model):

    instruction = models.ForeignKey(instruction)
    date_of_instruction = models.DateField()
    next_instruction = models.DateField()


    def __unicode__(self):
        return u"%s /odbyte - %s /następne - %s" % (self.instruction, self.date_of_instruction, self.next_instruction)


class Worker(models.Model):

    user = models.ForeignKey(User)
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=30)
    PESEL = models.CharField(max_length=11)
    course = models.ManyToManyField(Course)

    class Meta:
        ordering = ('course__next_instruction', 'Name')

    def __unicode__(self):
        return u"%s %s" % (self.Name, self.Surname)






