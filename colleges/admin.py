#import models
from django.contrib import admin
from colleges.models import School

class SchoolAdmin(admin.ModelAdmin):
  list_display = ['real_name']

admin.site.register(School, SchoolAdmin)