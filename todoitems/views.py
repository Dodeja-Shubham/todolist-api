from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins
from rest_auth.views import LoginView, LogoutView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import ToDoItemSerializer
from .models import ToDoItem
# Create your views here.

class ToDoItemView(generics.GenericAPIView,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin):
    '''
    View for User using Generic API View
    '''
    serializer_class = ToDoItemSerializer
    model = ToDoItem
    #queryset = ToDoItem.objects.all()
    lookup_field = 'id'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get(self, request, id=None):
        return self.list(request,id)
    
    def post(self, request):
        return self.create(request)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ToDoItem_Each_View(generics.GenericAPIView,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin):
    
    serializer_class = ToDoItemSerializer
    queryset = ToDoItem.objects.all()
    lookup_field = 'id'
    
    def get(self, request, id=None):
        return self.retrieve(request, id)
    
    def patch(self, request, id=None):
        return self.update(request, id)