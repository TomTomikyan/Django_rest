from rest_framework import serializers
from .models import category,car

class categorySerializers(serializers.ModelSerializer):

    class Meta:
        model = category
        fields = '__all__'

class carSerializers(serializers.ModelSerializer):

    class Meta:
        model = car
        fields = '__all__'