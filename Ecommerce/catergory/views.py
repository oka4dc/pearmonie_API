from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from products.models import Category
from rest_framework import status, generics
from rest_framework.views import APIView
from catergory.serializers import CartegorySerializers
from rest_framework.response import Response
from products.pagination import CustomPagination

# Create your views here.


class CatergoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CartegorySerializers


class CatergoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CartegorySerializers
    lookup_field = 'id'
