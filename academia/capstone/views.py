# built ins

# django-specific
from rest_framework import viewsets
# app-specific
from .serializers import CapstoneSerializer, SpecializationSerializer
from .models import Capstone, Specialization

class CapstoneViewSet(viewsets.ModelViewSet):

    queryset = Capstone.objects.all()
    serializer_class = CapstoneSerializer
        

class SpecializationViewSet(viewsets.ModelViewSet):

    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
