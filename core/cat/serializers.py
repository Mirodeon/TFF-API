from rest_framework import serializers
from core.clan.serializers import ClanSerializer
from core.user.models import Cat, CatOrigin, CatPosition, Clan
from core.user.serializers import UserInfoSerializer


class CatOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatOrigin
        fields = ['id', 'latitude', 'longitude']


class CatPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatPosition
        fields = ['id', 'latitude', 'longitude']


class CatSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.image_url', read_only=True)
    owner = UserInfoSerializer(source='user_id', read_only=True)
    clan = ClanSerializer(source='user_id.data.clan_id', read_only=True)
    position = CatPositionSerializer(read_only=True)
    origin = CatOriginSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = ['id', 'owner', 'clan', 'name', 'job', 'lvl', 'exp', 'limite_exp', 'timestamp', 'image', 'origin', 'position', 'alive', 'radius']


class CatFromClanSerializer(serializers.ModelSerializer):
    cats = serializers.SerializerMethodField()

    class Meta:
        model = Clan
        fields = ['id', 'name', 'effect_id', 'cats']

    def get_cats(self, obj):
        cats = Cat.objects.filter(user_id__data__clan_id=obj.id)

        return CatSerializer(cats, many = True).data