from django.db import models

# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)

    class Type(models.TextChoices):
        VENTE = 'vente'
        ACHAT = 'achat'
        PEREMPTION = 'peremption'
    type = models.CharField(max_length=100, choices=Type.choices, default=Type.VENTE)

    dateValidation = models.DateTimeField()
    total = models.FloatField()
    dateAjout = models.DateTimeField(auto_now_add=True)
    dateModif = models.DateTimeField(auto_now=True)
