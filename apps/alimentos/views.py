from django.shortcuts import render
from rest_framework import viewsets
from .models import Food
from .serializer import FoodSerializer
# Create your views here.


class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer