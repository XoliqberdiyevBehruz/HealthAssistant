from django.db import models

from apps.shared.models import BaseModel, Region


class ClinictCategory(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name 
    

class Clinic(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=250)
    working_days = models.CharField(max_length=250)
    working_hours = models.CharField(max_length=250)
    image = models.ImageField(upload_to="apps/clinics/clinic/image/", null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True)

    category = models.ForeignKey(ClinictCategory, on_delete=models.CASCADE, related_name='clinics')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='clinics')

    def __str__(self):
        return f'{self.name} - {self.address}'
