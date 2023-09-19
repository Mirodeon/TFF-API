from core.models import Cat, CatImage, InterestPoint, User
from rest_framework import serializers


class InterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestPoint
        fields = ['id', 'latitude', 'longitude']


class CatSerializer(serializers.ModelSerializer):
    url = CatImage.image_url
    owner = User.username

    class Meta:
        model = Cat
        fields = ['owner', 'name', 'job', 'lvl', 'exp', 'timestamp', 'url']
