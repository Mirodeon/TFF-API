from rest_framework import serializers
from core.models import Clan


class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ['id', 'name', 'effect_id']

