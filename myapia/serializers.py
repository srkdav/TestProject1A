from rest_framework import serializers

from .models import Hero,Details


class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ('hero_id','villian', 'universe')

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    details = DetailsSerializer(many=True)
    class Meta:
        model = Hero
        fields = ('hero_id','name', 'alias','details')