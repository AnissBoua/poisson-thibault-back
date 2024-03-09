from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
from quickstart.serializer.produit import ProduitSerializer
import json
from django.core import serializers
from math import ceil

class FruitDeMerList(APIView):
    def get(self, request, format=None):
        limit = request.GET.get('limit', 2)
        page = request.GET.get('page', 1)
        fruits = Produit.objects.filter(category=2)
        total = fruits.count()
        fruits = fruits[(int(page) - 1) * int(limit):int(page) * int(limit)]
        res = {
            'data': ProduitSerializer(fruits, many=True).data,
            'total': total,
            'limit': limit,
            'page': page,
            'last': ceil(total / int(limit))
        }
        return Response(res)
    
class FruitDeMerDetail(APIView):
    def get(self, request, pk, format=None):
        fruit = Produit.objects.get(pk=pk)
        fruit = json.loads(serializers.serialize('json', [fruit]))[0]['fields']
        return Response(fruit)