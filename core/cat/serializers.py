from rest_framework import serializers
from core.clan.serializers import ClanSerializer
from core.models import Cat, CatPosition, Clan, User
from core.user.serializers import UserInfoSerializer


class CatPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatPosition
        fields = ['id', 'latitude', 'longitude']


class CatSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='image.image_url', read_only=True)
    owner = UserInfoSerializer(source='user_id', read_only=True)
    clan = ClanSerializer(source='user_id.data.clan_id', read_only=True)
    position = CatPositionSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = ['id', 'owner', 'clan', 'name', 'job', 'lvl', 'exp', 'timestamp', 'url', 'position']


class CatFromClanSerializer(serializers.ModelSerializer):
    cats = serializers.SerializerMethodField()

    class Meta:
        model = Clan
        fields = ['id', 'name', 'cats']

    def get_cats(self, obj):
        cats = Cat.objects.filter(user_id__data__clan_id=obj.id)

        return CatSerializer(cats, many = True).data