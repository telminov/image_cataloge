from django.shortcuts import render, redirect
from rest_framework import viewsets
from core import models, serializers


def index(request):
    return redirect('/admin/')


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.Image
