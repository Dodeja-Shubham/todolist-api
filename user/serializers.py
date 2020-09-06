from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # Serializer for user model to store JSON Data
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(RegisterSerializer): 
    class Meta:
        model = User
        fields = ['username', 'full_name', 'mobile', 'email', 'password1', 'password2']

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        return email
    
    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data