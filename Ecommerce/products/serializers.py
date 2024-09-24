
from rest_framework import serializers
from .models import Products, Category
from products.currency_converter import CurrencyConverter


class ProductSerializers(serializers.ModelSerializer):
    
    converted_price = serializers.SerializerMethodField()
    class Meta:
        model = Products
        fields = ['id', 'Name', 'Price', 'Description', 'converted_price']
        
        
    def get_converted_price(self, obj):
        request = self.context.get('request')
        to_currency = request.query_params.get('currency', 'USD')  # Default to USD
        converter = CurrencyConverter()
        rate = converter.get_conversion_rate('USD', to_currency)
        return obj.price * rate if rate else obj.price
