from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer,DetailsSerializer
from .models import Hero,Details


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('hero_id')
    serializer_class = HeroSerializer

class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by('hero_id')
    serializer_class = DetailsSerializer