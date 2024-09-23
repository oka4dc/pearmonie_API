from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from products.models import Products
from rest_framework import status, generics
from rest_framework.views import APIView
from products.serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from products.pagination import CustomPagination
from django.conf import settings
from django.core.cache import cache
from products.permissions import IsSellerOrReadOnly
# Create your views here.

#CACHE_TTL = getattr(settings, 'CACHE_TTL', settings.CACHES['default']['TIMEOUT'])
CACHE_TIMEOUT = 60 * 5
class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    handles both viewing all and creating products 
    including permissions for both buyer and sellers users
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsSellerOrReadOnly]  # Apply custom permission


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsSellerOrReadOnly]  # Apply custom permission
    lookup_field = 'id'

 
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        cache_key = f"product_{product_id}"
        product = cache.get(cache_key)

        if not product:
            # Fetch product from the database if not in cache
            product = get_object_or_404(Products, pk=product_id)
            cache.set(cache_key, product, timeout=CACHE_TIMEOUT)

        # Increment product view count
        product.view_count += 1
        product.save()

        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

"""
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers

 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CartegorySerializers
""" 

"""
class productCreateRetreiveAll(APIView):
    
    def post (self, request):
        serializer_class = ProductSerializers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        user = Products.objects.all()
        serializer_class = ProductSerializers(user, many = True)
        pagination_class = CustomPagination
        return Response(data=serializer_class.data, status= status.HTTP_200_OK)
    
class ProductDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except:
            raise Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk, format = None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductSerializers(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
"""

class ProductSearch(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['Product_Name', 'Price']
  
