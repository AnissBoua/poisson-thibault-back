import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.consumers import WSConsumer
from quickstart.models import TransactionProduit
from quickstart.services.CAService import CAService
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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
            params['produit'] = produit
        if sale == 'true':
            params['sale'] = True

        transactionProduits = CAService.getTransactionProduitsBy(**params)
                
        cas = CAService.getCA(transactionProduits, startStr, endStr)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("ca_group", {"type": "send_message", "message": "Nouveau CA"})
        
        return Response(cas)
        