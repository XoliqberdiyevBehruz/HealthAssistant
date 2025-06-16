import django_filters

from apps.clinics.models import Clinic


class ClinicFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")
    class Meta:
        model = Clinic
        fields = ['name']
        