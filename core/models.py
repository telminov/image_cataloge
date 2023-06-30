from django.db import models


class Catalog(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    catalog = models.ForeignKey(Catalog, null=True, related_name='images', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    file = models.ImageField()

    def __str__(self):
        return self.name
