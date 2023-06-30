from rest_framework import viewsets
from core import models, serializers


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Catalog.objects.all()
    serializer_class = serializers.Catalog


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.Image
