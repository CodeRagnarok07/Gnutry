
from rest_framework import routers, serializers, viewsets
from .models import Origen, Food, Presentacion



class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'