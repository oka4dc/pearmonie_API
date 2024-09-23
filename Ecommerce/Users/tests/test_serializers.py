# tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

class ProductListViewTest(APITestCase):
    
    def setUp(self):
        """Create some products for testing"""
        Product.objects.create(name='Laptop', price=1000.00, stock=50)
        Product.objects.create(name='Phone', price=500.00, stock=100)

    def test_get_product_list(self):
        """Test if we can get the product list"""
        url = reverse('product-list')  # Assuming the URL pattern name is 'product-list'
        response = self.client.get(url)
        
        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that we got 2 products in the response
        self.assertEqual(len(response.data), 2)
        
        # Check that the first product name is 'Laptop'
        self.assertEqual(response.data[0]['name'], 'Laptop')
