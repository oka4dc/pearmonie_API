
from rest_framework import serializers
from .models import Products, Category

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'Name', 'Description', 'Price', 'Stock', 'Created_by']
        
class CartegorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
