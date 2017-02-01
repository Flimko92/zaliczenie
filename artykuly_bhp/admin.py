# coding: utf-8
from django.contrib import admin
from models import przydzial, produkty

class ProduktyAdmin(admin.ModelAdmin):
    pass

admin.site.register(produkty, ProduktyAdmin)

class PrzydzialAdmin(admin.ModelAdmin):
    pass

admin.site.register(przydzial, PrzydzialAdmin)