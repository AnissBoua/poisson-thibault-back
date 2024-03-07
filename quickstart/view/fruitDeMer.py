from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
import json
from django.core import serializers

class FruitDeMerList(APIView):
    def get(self, request, format=None):
        tab = []
        fruits = Produit.objects.all().values()
        for fruit in fruits:
            if fruit['category_id'] == 2:
                tab.append(fruit)
        return Response(tab)
    
class FruitDeMerDetail(APIView):
    def get(self, request, pk, format=None):
        fruit = Produit.objects.get(pk=pk)
        fruit = json.loads(serializers.serialize('json', [fruit]))[0]['fields']
        return Response(fruit)