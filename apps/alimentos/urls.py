from rest_framework import routers
from django.urls import path, include
from .views import FoodView


router = routers.DefaultRouter()
router.register(r'foods', FoodView)

urlpatterns = [
    path('', include(router.urls)),
]