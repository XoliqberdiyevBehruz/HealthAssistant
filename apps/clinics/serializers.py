from rest_framework import serializers

from apps.clinics import models 


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinic
        fields = [
            'id', 'name', 'address', 'working_days', 'working_hours', 'image', 'telegram_url'
        ]


class ClinicCategoryListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(method_name='get_count')

    class Meta:
        model = models.ClinictCategory
        fields = [
            'id', 'name', 'count'
        ]

    def get_count(self, obj):
        return obj.clinics.count()
    

class ClinicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinic
        fields = [
            'id', 'name', 'address', 'working_days', 'working_hours', 'image', 'telegram_url', 'description', 'phone'
        ]