from rest_framework import viewsets
from core import models, serializers


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Catalog.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CatalogShort
        if self.action == 'retrieve':
            return serializers.CatalogDetail


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.Image
