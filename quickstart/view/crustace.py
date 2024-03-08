from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
from quickstart.serializer.produit import ProduitSerializer
import json
from django.core import serializers

class CrustaceList(APIView):
    def get(self, request, format=None):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        crustaces = Produit.objects.filter(category=3)[(int(page) - 1) * int(limit):int(page) * int(limit)]
        crustaces = ProduitSerializer(crustaces, many=True).data
        return Response(crustaces)
    
class CrustaceDetail(APIView):
    def get(self, request, pk, format=None):
        crustace = Produit.objects.get(pk=pk)
        crustace = json.loads(serializers.serialize('json', [crustace]))[0]['fields']
        return Response(crustace)