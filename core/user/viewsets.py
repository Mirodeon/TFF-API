from core.user.serializers import UserDataCreateSerializer, UserDataSerializer, UserSerializer
from core.models import User, UserData
from rest_framework import viewsets
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['email']
    ordering = ['-email']

    def get_queryset(self):

        return User.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(id=lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj
    

class UserDataCreateViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = UserDataCreateSerializer
    filter_backends = [filters.OrderingFilter]

