from rest_framework import serializers

from apps.shared import models 


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
            'full_name', 'phone'
        ]


class ConsulationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consulation
        fields = [
            'id', 'full_name', 'phone', 'is_contacted', 'created_at',
        ]