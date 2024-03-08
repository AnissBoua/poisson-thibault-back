import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
from quickstart.serializer.produit import ProduitSerializer

class ProduitEndpoints(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            return self.getOne(request, pk, format)
        return self.getAll(request, format)
    
    def getOne(self, request, pk, format=None):
        produit = Produit.objects.get(pk=pk)
        produit = ProduitSerializer(produit).data
        return Response(produit)
    
    def getAll(self, request, format=None):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        produits = Produit.objects.select_related('category').all()[(int(page) - 1) * int(limit):int(page) * int(limit)]
        produits = ProduitSerializer(produits, many=True).data
        return Response(produits)
    
class ProduitsUpdates(APIView):
    def patch(self, request, format=None):
        data = json.loads(request.body)
        # Reorder data for easy access : [13 => {}, 15 => {}, 14 => {}]
        data = {produit['id']: produit for produit in data}

        ids = list(data.keys())
        produits = Produit.objects.filter(id__in=ids)
        for produit in produits:
            produitData = data[produit.id]
            if 'stockChange' in produitData:
                if produitData['stockChange'] == 'achat':
                    produit.stock += produitData['stock']
                else:
                    produit.stock -= produitData['stock']
            
            if produitData['prixSolde'] is not None and produitData['prixSolde'] != produit.prixSolde:
                produit.prixSolde = produitData['prixSolde']
                produit.onSale = True

            produit.save()
        produits = ProduitSerializer(produits, many=True).data
        return Response(produits)
        