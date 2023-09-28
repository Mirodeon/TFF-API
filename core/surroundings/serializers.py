from core.cat.serializers import CatSerializer
from core.models import InterestPoint
from rest_framework import serializers


class InterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestPoint
        fields = ['id', 'latitude', 'longitude']


class SurroundingsSerializer(serializers.ModelSerializer):
    interest_points = InterestPointSerializer(many=True)
    cats = CatSerializer(many=True)

    class Meta:
        fields = ['interest_points', 'cats']