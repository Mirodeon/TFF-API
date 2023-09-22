from rest_framework.routers import SimpleRouter
from core.surroundings.viewsets import SurroundingsAPIView
from core.user.viewsets import UserDataCreateViewSet, UserDataViewSet, UserDetailsViewSet, UserInfoViewSet, UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from django.urls import path, re_path


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='login')
routes.register(r'auth/register', RegistrationViewSet, basename='register')
routes.register(r'auth/refresh', RefreshViewSet, basename='refresh')

# USER
routes.register(r'user/create/data', UserDataCreateViewSet, basename='user-create-data')
routes.register(r'user/data', UserDataViewSet, basename='user-data')
routes.register(r'user/details', UserDetailsViewSet, basename='user-details')
routes.register(r'user/info', UserInfoViewSet, basename='user-info')
routes.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    *routes.urls,

    # SURROUNDINGS
    re_path(
        r'^surroundings/lat/(?P<lat>\d+\.\d+)/lon/(?P<lon>\d+\.\d+)/$',
        SurroundingsAPIView.as_view(),
        name='surroundings'
    )

]
