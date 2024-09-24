from rest_framework import serializers
from products.models import Products, Category


    
class StoreSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Store
        fields =[
            "Name"
        ] 