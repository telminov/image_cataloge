from rest_framework import serializers
from core import models


class Catalog(serializers.ModelSerializer):
    class Meta:
        model = models.Catalog
        fields = '__all__'


class Image(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'
