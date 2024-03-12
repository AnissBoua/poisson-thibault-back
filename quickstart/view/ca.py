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
        if request.GET.get('mounthly_ca') == 'true':
            return self.get_mounth_ca(request)
        
        if request.GET.get('margin') != None:
            return self.get_margin(request)

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
    
    def get_mounth_ca(self, request):
        mounth_ca = CAService.getThisMounthCA()
        return Response(mounth_ca)
    
    def get_margin(self, request):
        year = int(request.GET.get('margin'))
        margin = CAService.getYearlyMargin(year)
        response = {
            "margin": margin,
            "taxes" : margin * 0.3,
        }
        return Response(response)
        