import re

from rest_framework import generics
from rest_framework.response import Response

from apps.ai import serializers
from apps.common.utils import text_to_ai
from apps.doctors.serializers import DoctorListSerializer
from apps.clinics.serializers import ClinicListSerializer
from apps.doctors.models import Doctor
from apps.clinics.models import Clinic


class DescribeYourSymptomsApiView(generics.GenericAPIView):
    serializer_class = serializers.DescribeYourSymptomsSerializer
    queryset = None

    def post(self, request):
        serializer = serializers.DescribeYourSymptomsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            text = text_to_ai(serializer.data.get('text'))
            specialist = re.findall(r"\*\*(.*?)\*\*", text)
            return Response({"ai":text, "specialist": specialist})
        return Response(serializer.errors)


class FindDoctorAndClinicForSymtomsApiView(generics.GenericAPIView):
    serializer_class = serializers.DescribeYourSymptomsSerializer
    queryset = None

    def post(self, request):
        serializer = serializers.DescribeYourSymptomsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            specialist = serializer.data.get('text')
            doctors = Doctor.objects.filter(specialties__icontains=specialist)
            clinics = Clinic.objects.filter(doctors__specialties__icontains=specialist)
            return Response(
                {
                    "doctors": DoctorListSerializer(doctors, many=True).data,
                    "clinics": ClinicListSerializer(clinics, many=True).data
                }
            )
        return Response(serializer.errors)