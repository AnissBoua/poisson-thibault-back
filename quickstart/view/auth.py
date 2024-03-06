from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.serializers import UserSerializer

class Register(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Register")
        else : 
            print(serializer.errors)