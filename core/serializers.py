from rest_framework import serializers
from core import models


class CatalogShort(serializers.ModelSerializer):
    top_images = serializers.SerializerMethodField()

    class Meta:
        model = models.Catalog
        fields = '__all__'

    def get_top_images(self, obj: models.Catalog):
        return Image(instance=obj.images.all()[:5], many=True).data


class CatalogDetail(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = models.Catalog
        fields = '__all__'

    def get_images(self, obj: models.Catalog):
        return Image(instance=obj.images.all(), many=True).data


class Image(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
