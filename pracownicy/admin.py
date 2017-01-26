from django.contrib import admin

from .models import Worker

class WorkerAdmin(admin.ModelAdmin):
 search_fields = ['Name','Surname']
 order_by = ['Surname']
# Register your models here.

admin.site.register(Worker, WorkerAdmin)
#admin.site.register([Worker])





