import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import TransactionProduit
from quickstart.services.CAService import CAService

class CAEndpoints(APIView):
    def get(self, request, pk=None, format=None):
        startStr = request.GET.get('start')
        endStr = request.GET.get('end')
        category = request.GET.get('category')
        produit = request.GET.get('produit')
        if category:
            transactionProduits = CAService.getTransactionProduitsBy(startStr, endStr, category=category)
        elif produit:
            transactionProduits = CAService.getTransactionProduitsBy(startStr, endStr, Produit=produit)
        else:
            transactionProduits = CAService.getTransactionProduitsBy(startStr, endStr)
                
        cas = CAService.getCA(transactionProduits, startStr, endStr)
        
        return Response(cas)
        