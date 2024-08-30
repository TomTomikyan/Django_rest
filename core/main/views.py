from django.shortcuts import render
from rest_framework import viewsets
from .serializers import carSerializers, categorySerializers
from .models import category,car

# Create your views here.

class categoryView(viewsets.ModelViewSet):

    queryset = category.objects.all()
    serializer_class = categorySerializers

class carView(viewsets.ModelViewSet):

    queryset = car.objects.all()
    serializer_class = carSerializers