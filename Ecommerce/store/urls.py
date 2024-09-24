from django.urls import path, include
from store.views import (
    StoreListCreateAPIView,
    StoreRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('store/', StoreListCreateAPIView.as_view(), name='catergory'),
    path('store/<int:id>/',StoreRetrieveUpdateDestroyAPIView.as_view(), name='catergory_update'),
    
]