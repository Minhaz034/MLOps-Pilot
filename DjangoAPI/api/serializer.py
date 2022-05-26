from rest_framework import serializers
from .models import Features

class FeaturesSerializer(serializers.ModelSerializer):
    class meta:
        model = Features
        fields ='__all__'