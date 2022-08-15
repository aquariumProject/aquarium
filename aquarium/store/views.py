from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Item
from .serializer import ItemSerializer

# Create your views here.

class ItemList(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class=ItemSerializer

    def get_queryset(self):
        return Item.objects.all().order_by('item_code')

    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

class ItemDetail(generics.GenericAPIView,mixins.RetrieveModelMixin):
    serializer_class=ItemSerializer

    def get_queryset(self):
        return Item.objects.all().order_by('item_code')

    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
