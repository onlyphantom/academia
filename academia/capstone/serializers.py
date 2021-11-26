from rest_framework import serializers
from .models import Specialization, Capstone

class SpecializationSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Specialization
        fields = ('id', 'description', 'name', 'num_hours')

class CapstoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Capstone
        fields = '__all__'
