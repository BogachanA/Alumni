from django.contrib import admin
from .models import *

# Register your models here.


class GraduateAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','year_graduated')
    ordering = ('last_name',)


class UniAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Alumni,GraduateAdmin)
admin.site.register(University,UniAdmin)