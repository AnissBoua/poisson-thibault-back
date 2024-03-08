from rest_framework import serializers
from quickstart.models import Produit
from .category import CategorySerializer

class ProduitSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    pourcentage = serializers.SerializerMethodField()

    def get_pourcentage(self, obj):
        if obj.prixSolde is not None:
            pourcentage = ((obj.prix - obj.prixSolde) / obj.prix) * 100
            return round(pourcentage, 2)
        return None

    class Meta:
        model = Produit
        fields = ['id', 'nom', 'prix', 'prixSolde', 'stock', 'commentaire', 'onSale', 'dateAjout', 'dateModif', 'category', 'pourcentage']