from core.models import Clan, User, UserData
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']
        read_only_field = ['is_active']


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'is_active']
        read_only_field = ['is_active']


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


class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ['id', 'name']


class UserDataSerializer(serializers.ModelSerializer):
    clan = ClanSerializer(source='clan_id', read_only=True)

    class Meta:
        model = UserData
        fields = ['clan', 'food']


class UserDetailsSerializer(serializers.ModelSerializer):
    data = UserDataSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'data']
