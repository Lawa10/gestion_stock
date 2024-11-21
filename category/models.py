from django.db import models
from django.db.models import Model


# Create your models here.
class Category(models.Model):
    nomCategory =models.CharField(max_length=100)
    desCategory = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nomCategory

