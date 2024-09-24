from rest_framework import serializers
from store.models import Store

  
class StoreSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model =Store
        fields =[
            "Name", "Updated_at", "created_at", "Description", "Address"
        ] 