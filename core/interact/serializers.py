from rest_framework import serializers
from core.models import InteractCat, InteractInterestPoint
from core.user.serializers import UserInfoSerializer


class InteractCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractCat
        fields = ['id', 'timestamp', 'given_food']


class InteractCatWithUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer(source='user_id', read_only=True)

    class Meta:
        model = InteractCat
        fields = ['id', 'timestamp', 'given_food', 'user']


class InteractInterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InteractInterestPoint
        fields = ['id', 'timestamp']