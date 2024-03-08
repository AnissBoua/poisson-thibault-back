from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Category

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all().values()
        return Response(categories)