from django.db import models


class Categories(models.Model):
    id = models.ForeignKey
    name = models.CharField(max_length=100)
