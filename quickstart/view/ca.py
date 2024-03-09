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
        sale = request.GET.get('sale')

        params = {'start_str': startStr, 'end_str': endStr}

        if category:
            params['category'] = category
        if produit:
            params['Produit'] = produit
        if sale:
            params['sale'] = True

        transactionProduits = CAService.getTransactionProduitsBy(**params)
                
        cas = CAService.getCA(transactionProduits, startStr, endStr)
        
        return Response(cas)
        