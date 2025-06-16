from django.core.exceptions import ValidationError

from rest_framework import generics, status
from rest_framework.response import Response

from django_filters.rest_framework.backends import DjangoFilterBackend

from apps.clinics import models, serializers, filters


class ClinicCategoryListApiView(generics.ListAPIView):
    serializer_class = serializers.ClinicCategoryListSerializer
    queryset = models.ClinictCategory.objects.all()
    

class ClinicListApiView(generics.ListAPIView):
    queryset = models.Clinic.objects.all()
    serializer_class = serializers.ClinicListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ClinicFilter

    def get_queryset(self):
        try:
            category = models.ClinictCategory.objects.get(id=self.kwargs.get('id'))
        except models.ClinictCategory.DoesNotExist:
            raise ValidationError("Category not found", code=404) 
        return self.filter_queryset(self.queryset.filter(category=category))