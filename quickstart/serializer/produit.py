from rest_framework import serializers
from quickstart.models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'name', 'description', 'price', 'category', 'stock', 'onSale', 'dateAjout', 'dateModif']