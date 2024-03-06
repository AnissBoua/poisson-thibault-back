from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
import json
from django.core import serializers

class ProduitList(APIView):
    def get(self, request, format=None):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        produits = Produit.objects.all()[(int(page) - 1) * int(limit):int(page) * int(limit)].values()
        return Response(produits)
    
class ProduitDetail(APIView):
    def get(self, request, pk, format=None):
        produit = Produit.objects.get(pk=pk)
        produit = json.loads(serializers.serialize('json', [produit]))[0]['fields']
        return Response(produit)