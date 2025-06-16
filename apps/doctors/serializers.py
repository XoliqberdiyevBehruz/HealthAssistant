from rest_framework import serializers

from apps.doctors import models 
from apps.clinics.serializers import ClinicSerializer


class DoctorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DoctorCategory
        fields = [
            'id', 'name'
        ]

    
class DoctorListSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer()
    category = DoctorCategorySerializer()

    class Meta:
        model = models.Doctor
        fields = [
            'id', 'first_name', 'last_name', 'middle_name', 'photo', 'specialties',
            'experience_years', 'initial_consultation_price', 'follow_up_consultation_price', 'rating', 'phone_number', 'telegram_url', 'clinic', 'category'
        ]


class DoctorDetailSerializer(serializers.ModelSerializer):
    clinic = serializers.SerializerMethodField(method_name='get_clinic')

    class Meta:
        model = models.Doctor
        fields = [
            'id', 'first_name', 'last_name', 'middle_name', 'photo', 'specialties', 'experience_years', 'initial_consultation_price', 'follow_up_consultation_price', 'phone_number', 'telegram_url', 'description', 'clinic'
        ]
    
    def get_clinic(self, obj):
        return {
                "name": obj.clinic.name,
                "address": obj.clinic.address
            }