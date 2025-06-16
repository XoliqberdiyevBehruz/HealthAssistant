from django.contrib import admin

from apps.clinics import models 

admin.site.register(models.Clinic)
admin.site.register(models.ClinictCategory)
