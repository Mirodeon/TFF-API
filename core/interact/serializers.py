from rest_framework import serializers
from core.models import InteractCat, InteractInterestPoint


class InteractCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractCat
        fields = ['id', 'timestamp', 'given_food']


class InteractInterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractInterestPoint
        fields = ['id', 'timestamp']