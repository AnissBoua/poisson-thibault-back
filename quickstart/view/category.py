from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Category

class CategoryEndpoints(APIView):
    def get(self, request, pk=None, format=None):
        categories = Category.objects.all().values()
        return Response(categories)