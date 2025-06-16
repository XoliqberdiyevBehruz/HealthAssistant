from django.core.exceptions import ValidationError
from django.db.models import Q

import django_filters

from apps.doctors import models 
from apps.shared.models import Region

class DoctorFilter(django_filters.FilterSet):
    region = django_filters.UUIDFilter(method='filter_by_region')
    name = django_filters.CharFilter(method='filter_by_name')

    class Meta:
        model = models.Doctor
        fields = ['region', 'name']
    
    def filter_by_region(self, queryset, name, value):
        try:
            region = Region.objects.get(id=value)
        except Region.DoesNotExist:
            raise ValidationError("region not found")
        return queryset.filter(clinic__region=region)
    
    def filter_by_name(self, queryset, name, value):
        return queryset.filter(Q(first_name__icontains=value) | Q(last_name=value) | Q(middle_name=value))