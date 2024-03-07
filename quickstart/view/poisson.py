from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
import json
from django.core import serializers

class PoissonList(APIView):
    def get(self, request, format=None):
        tab = []
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        poissons = Produit.objects.all()[(int(page) - 1) * int(limit):int(page) * int(limit)].values()
        for poisson in poissons:
            if poisson['category_id'] == 1:
                tab.append(poisson)
        return Response(tab)
    
class PoissonDetail(APIView):
    def get(self, request, pk, format=None):
        poisson = Produit.objects.get(pk=pk)
        poisson = json.loads(serializers.serialize('json', [poisson]))[0]['fields']
        return Response(poisson)