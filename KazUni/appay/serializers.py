from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import ModelPays

class ModelPaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPays
        fields = '__all__'

