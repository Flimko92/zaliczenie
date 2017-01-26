from __future__ import unicode_literals


from django.db import models
#from django.contrib.auth.models import AbstractUser

class Worker(models.Model):
	Name = models.CharField(max_length=20)
	Surname = models.CharField(max_length=30)
	PESEL = models.CharField(max_length=11)
	def __str__(self):
		return "{Name} {Surname}".format(Name=self.Name,Surname=self.Surname)
# Create your models here.
