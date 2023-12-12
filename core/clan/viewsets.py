from rest_framework import filters
from rest_framework import viewsets
from core.cat.serializers import CatFromClanSerializer
from core.clan.serializers import ClanSerializer
from core.models import Cat, Clan
from core.surroundings.serializers import CatSerializer
from core.user.serializers import UserFromClanSerializer


class ClanViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = ClanSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
    ordering = ['-name']

    def get_queryset(self):

        return Clan.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Clan.objects.get(id=lookup_field_value)

        return obj


class UserFromClanViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserFromClanSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):

        return Clan.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Clan.objects.filter(data__clan_id=lookup_field_value)

        return obj
    

class CatFromClanViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CatFromClanSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):

        return Clan.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Cat.objects.get(user_id__data__clan_id=lookup_field_value)

        return obj
