from django.contrib import admin
from core import models


@admin.register(models.Catalog)
class Catalog(admin.ModelAdmin):
    search_fields = ('name', )


@admin.register(models.Image)
class Image(admin.ModelAdmin):
    list_display = ('name', 'file', 'catalog')
    list_filter = ('catalog__name', )
    search_fields = ('name', )
