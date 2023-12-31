from core.clan.serializers import ClanSerializer
from core.models import Clan, User, UserData, UserImage
from rest_framework import serializers
from core.utils import getAvatarImgAI, getColorClan, uploadImgToCloud


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


class UserDataSerializer(serializers.ModelSerializer):
    clan = ClanSerializer(source='clan_id', read_only=True)
    image = serializers.CharField(source='image.image_url', read_only=True)

    class Meta:
        model = UserData
        fields = ['clan', 'food', 'limite_food', 'lvl', 'exp', 'limite_exp', 'image']

    def create(self, validated_data):
        request = self.context.get("request")

        user_data_instance = UserData.objects.create(
            user_id=request.user,
            clan_id=Clan.objects.get(id=request.data['clan_id'])
        )
        
        color = getColorClan(user_data_instance.clan_id.name) 
        image_response = getAvatarImgAI(color, request.data['animal'], request.data['landscape'], request.data['hobby'])

        image_ref = UserImage.objects.create(
            user_data_id=user_data_instance,
            seed=image_response["seed"]
        )
        uploadImgToCloud(str(image_ref.image_uuid), image_response["image"])

        return user_data_instance


class UserDetailsSerializer(serializers.ModelSerializer):
    data = UserDataSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'is_active', 'data']


class UserFromClanSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = Clan
        fields = ['id', 'name', 'effect_id', 'users']

    def get_users(self, obj):
        users = User.objects.filter(data__clan_id=obj.id)

        return UserInfoSerializer(users, many = True).data
