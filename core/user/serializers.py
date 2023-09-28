from core.clan.serializers import ClanSerializer
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


class UserFromClanSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Clan
        fields = ['id', 'name', 'users']

    def get_users(self, obj):
        users = User.objects.filter(data__clan_id=obj.id)

        return UserInfoSerializer(users, many = True).data
