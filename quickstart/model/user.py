from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    dateAjout = models.DateTimeField(auto_now_add=True)
    dateModif = models.DateTimeField(auto_now=True)
    