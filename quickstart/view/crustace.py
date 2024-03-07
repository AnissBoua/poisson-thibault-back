from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
import json
from django.core import serializers

class CrustaceList(APIView):
    def get(self, request, format=None):
        tab = []
        crustaces = Produit.objects.all().values()
        for crustace in crustaces:
            if crustace['category_id'] == 3:
                tab.append(crustace)
        return Response(tab)
    
class CrustaceDetail(APIView):
    def get(self, request, pk, format=None):
        crustace = Produit.objects.get(pk=pk)
        crustace = json.loads(serializers.serialize('json', [crustace]))[0]['fields']
        return Response(crustace)