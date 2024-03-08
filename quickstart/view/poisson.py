from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
from quickstart.serializer.produit import ProduitSerializer
import json
from django.core import serializers

class PoissonList(APIView):
    def get(self, request, format=None):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        poissons = Produit.objects.filter(category=1)[(int(page) - 1) * int(limit):int(page) * int(limit)]
        poissons = ProduitSerializer(poissons, many=True).data
        return Response(poissons)
    
class PoissonDetail(APIView):
    def get(self, request, pk, format=None):
        poisson = Produit.objects.get(pk=pk)
        poisson = json.loads(serializers.serialize('json', [poisson]))[0]['fields']
        return Response(poisson)