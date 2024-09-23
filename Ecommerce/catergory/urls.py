from django.urls import path, include
from catergory.views import (
    CatergoryListCreateAPIView,
    CatergoryRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('catergory/', CatergoryListCreateAPIView.as_view(), name='catergory'),
    path('catergory/<int:id>/',CatergoryRetrieveUpdateDestroyAPIView.as_view(), name='catergory_update'),
    
]