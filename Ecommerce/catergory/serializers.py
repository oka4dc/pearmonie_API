from rest_framework import serializers
from catergory.models import Category

  
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