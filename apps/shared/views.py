from rest_framework import generics

from apps.shared import models, serializers


class RegionListApiView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionListSerializer
    