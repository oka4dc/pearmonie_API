from django.urls import path, include
from products.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    CatergoryListCreateAPIView,
    CatergoryRetrieveUpdateDestroyAPIView
)
from rest_framework.routers import DefaultRouter
"""
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductListView)
router.register('products/<int:pk>/', ProductDetailView)
"""
urlpatterns = [
    #path('', include(router.urls)),
    #path('CreateProduct/', productCreateRetreiveAll.as_view(), name='CreateProduct'),
    path('products/', ProductListCreateAPIView.as_view(), name='products'),
    path('product/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='DeleteProduct'),
    path('catergory/', CatergoryListCreateAPIView.as_view(), name='products'),
    path('catergory/<int:id>/',CatergoryRetrieveUpdateDestroyAPIView.as_view(), name='DeleteProduct'),
    #path('UpdateProduct/', ProductDetail.as_view(), name='UpdateProduct'),
]