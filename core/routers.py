from rest_framework.routers import SimpleRouter
from core.clan.viewsets import CatFromClanViewSet, ClanViewSet, UserFromClanViewSet
from core.interact.viewsets import InteractWithCat, InteractWithInterestPoint
from core.surroundings.viewsets import SurroundingsAPIView
from core.user.viewsets import UserDataViewSet, UserDetailsViewSet, UserInfoViewSet, UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from django.urls import path


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='login')
routes.register(r'auth/register', RegistrationViewSet, basename='register')
routes.register(r'auth/refresh', RefreshViewSet, basename='refresh')

# USER
routes.register(r'user/data', UserDataViewSet, basename='user-data')
routes.register(r'user/details', UserDetailsViewSet, basename='user-details')
routes.register(r'user/info', UserInfoViewSet, basename='user-info')
routes.register(r'user', UserViewSet, basename='user')

# CLAN
routes.register(r'clan/user', UserFromClanViewSet, basename='user-from-clan')
routes.register(r'clan/cat', CatFromClanViewSet, basename='cat-from-clan')
routes.register(r'clan', ClanViewSet, basename='clan')


urlpatterns = [
    *routes.urls,

    # SURROUNDINGS
    path(r'surroundings', SurroundingsAPIView.as_view(), name='surroundings'),

    # INTERACT
    path(r'interact/interest', InteractWithInterestPoint.as_view(), name='interact-interest'),
    path(r'interact/cat', InteractWithCat.as_view(), name='interact-cat')

]
