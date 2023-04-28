from django.db import models


class ADS(models.Model):
    id = models.ForeignKey
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()
