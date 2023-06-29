from django.contrib import admin
from core import models


@admin.register(models.Image)
class Image(admin.ModelAdmin):
    list_display = ('name', 'file')
