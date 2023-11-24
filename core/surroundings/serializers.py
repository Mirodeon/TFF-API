from core.cat.serializers import CatOriginSerializer, CatPositionSerializer, CatSerializer
from core.clan.serializers import ClanSerializer
from core.interact.serializers import InteractCatSerializer, InteractInterestPointSerializer
from core.models import Cat, InterestPoint, InteractCat, InteractInterestPoint
from rest_framework import serializers
from core.user.serializers import UserInfoSerializer


class InterestPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestPoint
        fields = ['id', 'latitude', 'longitude']


class InterestPointWithInteractSerializer(serializers.ModelSerializer):
    interact = serializers.SerializerMethodField()

    class Meta:
        model = InterestPoint
        fields = ['id', 'latitude', 'longitude', 'interact']
    
    def get_interact(self, obj):
        interact = InteractInterestPoint.objects.filter(user_id=self.context.get("request").user, interest_point_id=obj)

        return InteractInterestPointSerializer(interact, many=True).data
    


class CatWithInteractSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='image.image_url', read_only=True)
    owner = UserInfoSerializer(source='user_id', read_only=True)
    clan = ClanSerializer(source='user_id.data.clan_id', read_only=True)
    position = CatPositionSerializer(read_only=True)
    origin = CatOriginSerializer(read_only=True)
    interact = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = ['id', 'owner', 'clan', 'name', 'job', 'lvl', 'exp', 'timestamp', 'url', 'origin', 'position', 'interact']

    def get_interact(self, obj):
        interact = InteractCat.objects.filter(user_id=self.context.get("request").user, cat_id=obj)

        return InteractCatSerializer(interact, many=True).data