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