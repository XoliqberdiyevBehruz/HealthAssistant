from django.contrib import admin

from apps.doctors import models

admin.site.register(models.Doctor)
admin.site.register(models.DoctorCategory)
