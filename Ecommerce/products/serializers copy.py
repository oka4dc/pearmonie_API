from rest_framework import serializers
from products.models import Products, Category


class ProductSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Products
        fields = ['id', 'name', 'price', 'description']  # Ensure 'name' is spelled correctly here

    
class CartegorySerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Category
        fields =[
            "title"
        ] 