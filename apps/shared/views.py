from rest_framework import generics

from apps.shared import models, serializers


class RegionListApiView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionListSerializer
    

class ConsulationCreateApiView(generics.CreateAPIView):
    queryset = models.Consulation.objects.all()
    serializer_class = serializers.ConsulationCreateSerializer


class ConsulationCreateApiView(generics.ListAPIView):
    queryset = models.Consulation.objects.order_by('created_at')
    serializer_class = serializers.ConsulationListSerializer