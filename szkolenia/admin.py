# coding: utf-8
from django.contrib import admin
from models import documentation, instruction


class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')
    pass

admin.site.register(documentation, DocumentationAdmin)

class InstructionAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')
    pass

admin.site.register(instruction, InstructionAdmin)
