# coding: utf-8
from django.contrib import admin
from models import alert

class AlertAdmin(admin.ModelAdmin):
    pass

admin.site.register(alert, AlertAdmin)