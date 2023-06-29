from django.urls import path
from rest_framework.routers import DefaultRouter

import core.views

urlpatterns = [
    path('', core.views.index),
]


router = DefaultRouter()
router.register('images', core.views.ImageViewSet, basename='images')
urlpatterns += router.urls
