from django.shortcuts import render

from rest_framework import generics
from rest_framework import mixins
from rest_auth.views import LoginView, LogoutView

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
    queryset = ToDoItem.objects.all()
    lookup_field = 'id'

    def get(self, request):
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

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