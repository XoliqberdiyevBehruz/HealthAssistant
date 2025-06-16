from collections import defaultdict

from rest_framework import status, generics, views
from rest_framework.response import Response

from django_filters.rest_framework.backends import DjangoFilterBackend

from apps.doctors import serializers, models, filters


class DoctorCategoryListApiView(views.APIView):
    def get(self, request):
        categories = models.DoctorCategory.objects.order_by('name')
        grouped = defaultdict(list)

        for category in categories:
            first_letter = category.name[0].upper()
            category_dict = {"id": category.id, "name": category.name}
            grouped[first_letter].append(category_dict)

        grouped_list = sorted(grouped.items())

        return Response(grouped_list, status=status.HTTP_200_OK)


class DoctorListApiView(generics.GenericAPIView):
    serializer_class = serializers.DoctorListSerializer
    queryset = models.Doctor.objects.select_related("clinic", 'category')
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.DoctorFilter

    def get(self, request, category_id):
        try:
            category = models.DoctorCategory.objects.get(id=category_id)
        except models.DoctorCategory.DoesNotExist:
            return Response({"message": "category not found"}, status=status.HTTP_404_NOT_FOUND)

        doctors = models.Doctor.objects.filter(category=category).select_related("clinic", 'category')

        queryset = self.filter_queryset(doctors)
        serializer = serializers.DoctorListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DoctorDetailApiView(views.APIView):
    def get(self, request, id):
        try:
            doctor = models.Doctor.objects.select_related('clinic').get(id=id)
        except models.Doctor.DoesNotExist:
            return Response({"message": "Doctor not dound"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.DoctorDetailSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

