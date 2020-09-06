from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import mixins
from rest_auth.views import LoginView, LogoutView

from .serializers import UserSerializer
# Create your views here.

class UserView(generics.GenericAPIView,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin):
    '''
    View for User using Generic API View
    '''
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def get(self, request):
            return self.list(request)

class User_Each_View(generics.GenericAPIView,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    
    def get(self, request, id=None):
        return self.retrieve(request, id)
    
    def put(self, request, id=None):
        return self.update(request, id)

class UserLogin(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "User has logged in", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

class UserLogout(LogoutView):
    def get_response(self):
        orginal_response = super().get_response()
        return orginal_response
