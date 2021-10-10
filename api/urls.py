from django.urls import path
from .views import *

urlpatterns = [
    path("test1",CreateTest.as_view(),name="apitest1"),
    path("test2",Test2.as_view(),name="apitest2"),
    path("cart",HandleCart.as_view(),name="cart"),
]
