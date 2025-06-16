from rest_framework import serializers

from apps.shared import models 


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = [
            'id', 'name'
        ]