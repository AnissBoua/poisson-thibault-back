from rest_framework import serializers
from quickstart.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'email', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Crée et retourne un nouvel utilisateur avec le mot de passe haché
        return User.objects.create_user(**validated_data)