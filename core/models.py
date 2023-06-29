from django.db import models


class Image(models.Model):
    name = models.CharField('Название', max_length=255)
    file = models.ImageField()

    def __str__(self):
        return self.name
