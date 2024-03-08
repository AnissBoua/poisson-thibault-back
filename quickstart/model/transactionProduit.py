from django.db import models

# Create your models here.
class TransactionProduit(models.Model):
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey('Transaction', on_delete=models.DO_NOTHING)
    produit = models.ForeignKey('Produit', on_delete=models.DO_NOTHING)
    prix = models.FloatField()
    prixSolde = models.FloatField(null=True)
    quantity = models.IntegerField()
    ca = models.FloatField()
