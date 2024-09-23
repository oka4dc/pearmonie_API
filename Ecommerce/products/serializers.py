
from rest_framework import serializers
from .models import Products, Category

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("__all__")
        
class CartegorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
