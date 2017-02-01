# coding: utf-8
from django.contrib import admin

from .models import Worker, Course

class WorkerAdmin(admin.ModelAdmin):
 search_fields = ['Name','Surname']
 order_by = ['Surname']

admin.site.register(Worker, WorkerAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)




