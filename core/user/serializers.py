from core.models import Clan, User, UserData
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']
        read_only_field = ['is_active']


class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ['id', 'name']


class UserDataCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ['clan_id']

    def create(self, validated_data):
        request = self.context.get("request")

        user_data_instance = UserData.objects.create(
            user_id=request.user,
            clan_id=validated_data['clan_id']
        )

        return user_data_instance
