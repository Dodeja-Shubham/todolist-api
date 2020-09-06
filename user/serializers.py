from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Serializer for user model to store JSON Data
    class Meta:
        model = User
        fields = '__all__'
