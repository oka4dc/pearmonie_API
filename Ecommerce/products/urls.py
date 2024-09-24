from django.urls import path, include
from products.views import (
    ProductListAPIView,
    ProductCreateview,
    ProductRetrieveUpdateDestroyAPIView,
)
#from rest_framework.routers import DefaultRouter
"""
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductListView)
router.register('products/<int:pk>/', ProductDetailView)
"""
urlpatterns = [
    #path('', include(router.urls)),
    #path('CreateProduct/', productCreateRetreiveAll.as_view(), name='CreateProduct'),
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('create-products/', ProductCreateview.as_view(), name='create-products'),
    path('product/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='DeleteProduct'),
    #path('UpdateProduct/', ProductDetail.as_view(), name='UpdateProduct'),
]