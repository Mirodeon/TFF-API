from core.models import Cat, CatPosition, InterestPoint
from rest_framework import serializers


class InterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestPoint
        fields = ['id', 'latitude', 'longitude']


class CatPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatPosition
        fields = ['id', 'latitude', 'longitude']


class CatSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='image.image_url', read_only=True)
    owner = serializers.CharField(source='user_id.username', read_only=True)
    clan = serializers.CharField(source='user_id.user_data.clan.name', read_only=True)
    position = CatPositionSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = ['id', 'owner', 'clan', 'name', 'job', 'lvl', 'exp', 'timestamp', 'url', 'position']

class SurroundingsSerializer(serializers.ModelSerializer):
    interest_points = InterestPointSerializer(many=True)
    cats = CatSerializer(many=True)

    class Meta:
        fields = ['interest_points', 'cats']