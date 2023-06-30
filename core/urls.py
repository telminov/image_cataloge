from django.urls import path
from rest_framework.routers import DefaultRouter

import core.views

urlpatterns = [
]


router = DefaultRouter()
router.register('catalogs', core.views.CatalogViewSet, basename='catalogs')
router.register('images', core.views.ImageViewSet, basename='images')
urlpatterns += router.urls
