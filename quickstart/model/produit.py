from django.db import models

# Create your models here.
class Produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prix = models.FloatField()
    prixSolde = models.FloatField(null=True, blank=True)
    stock = models.IntegerField()
    commentaire = models.TextField()
    onSale = models.BooleanField(default=False)
    dateAjout = models.DateTimeField(auto_now_add=True)
    dateModif = models.DateTimeField(auto_now=True)

    # Reference to Category
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
