from django.db import models

from apps.shared.models import BaseModel
from apps.clinics.models import Clinic


class DoctorCategory(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name 
    

class Doctor(BaseModel):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='apps/doctors/doctor/photo/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    specialties = models.TextField()

    experience_years = models.PositiveIntegerField(default=0)
    initial_consultation_price = models.PositiveBigIntegerField(default=0)
    follow_up_consultation_price = models.PositiveBigIntegerField(default=0)

    rating = models.FloatField(default=0.0)
    phone_number = models.CharField(max_length=15, unique=True)
    telegram_url = models.URLField(null=True, blank=True)

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctors')
    category = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.rating}'
    