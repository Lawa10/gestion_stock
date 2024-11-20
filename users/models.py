# Django imports
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser


# class UserProfile(models.Model):
#     ROLE_CHOICES = (
#         ('gestionnaire', 'Gestionnaire'),
#         ('vendeur', 'Vendeur')
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
