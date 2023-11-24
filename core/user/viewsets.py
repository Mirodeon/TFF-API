from core.user.serializers import UserDataCreateSerializer, UserDataSerializer, UserDetailsSerializer, UserInfoSerializer, UserSerializer
from core.models import User, UserData
from rest_framework import viewsets
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['email']
    ordering = ['-email']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(id=lookup_field_value)

        return obj
    

class UserInfoViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserInfoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username']
    ordering = ['-username']

    def get_queryset(self):
        
        return User.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(id=lookup_field_value)

        return obj


class UserDataViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = UserDataSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):

        return UserData.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = UserData.objects.get(user_id=lookup_field_value)

        return obj


class UserDetailsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserDetailsSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):

        return User.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get(id=lookup_field_value)

        return obj
