from django.urls import path
from .views import ItemList

urlpatterns=[
    path("ItemList/", ItemList.as_view(), name="ItemList"),
    #path("store/<", ItemList.as_view(), name="ItemList"),
    
]