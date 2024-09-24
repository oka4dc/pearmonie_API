from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from store.models import Store
from rest_framework import status, generics
from rest_framework.views import APIView
from store.serializers import StoreSerializers
from rest_framework.response import Response
#from products.pagination import CustomPagination

# Create your views here.


class StoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class StoreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    lookup_field = 'id'

