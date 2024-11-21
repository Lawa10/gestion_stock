from django.db import models

from ..category.models import Category


# Create your models here.
class SubCategory(models.Model):
    nomSubCategory = models.CharField(max_length=100)
    desSubCategory = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  # Supprime les sous-catégories si la catégorie est supprimée
        related_name="subcategories"  # Facilite les requêtes inversées
    )

    def __str__(self):
        return self.nomSubCategory