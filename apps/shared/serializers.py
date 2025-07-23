from rest_framework import serializers

from apps.shared import models 
from apps.doctors.serializers import DoctorListSerializer


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = [
            'id', 'name'
        ]

    
class ConsulationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consulation
        fields = [
            'full_name', 'phone', 'doctor'
        ]


class ConsulationListSerializer(serializers.ModelSerializer):
    doctor = DoctorListSerializer()
    
    class Meta:
        model = models.Consulation
        fields = [
            'id', 'full_name', 'phone', 'is_contacted', 'doctor', 'created_at',
        ]