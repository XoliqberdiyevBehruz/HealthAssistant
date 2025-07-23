import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True 

    
class Region(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
    

class Consulation(BaseModel):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='doctors', null=True)
    is_contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.phone
    
