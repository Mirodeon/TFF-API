from django.contrib import admin
from .models import CatOrigin, User, Clan, UserData, UserImage, UserPosition, Cat, CatImage, CatPosition, InterestPoint, InteractCat, InteractInterestPoint


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = [
        'email',
        'username'
    ]


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    search_fields = [
        'name'
    ]


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id__email',
        'user_id__username',
        'clan_id__name'
    ]


@admin.register(UserPosition)
class UserPositionAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id__email',
        'user_id__username',
        'longitude',
        'latitude'
    ]


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    search_fields = [
        'user_data_id__user_id__email',
        'user_data_id__user_id__username',
        'user_data_id__clan_id__name',
        'cat_id__job',
        'image_uuid'
    ]


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id__email',
        'user_id__username',
        'name',
        'job'
    ]


@admin.register(CatImage)
class CatImageAdmin(admin.ModelAdmin):
    search_fields = [
        'cat_id__user_id__email',
        'cat_id__user_id__username',
        'cat_id__name',
        'cat_id__job',
        'image_uuid'
    ]


@admin.register(CatPosition)
class CatPositionAdmin(admin.ModelAdmin):
    search_fields = [
        'cat_id__user_id__email',
        'cat_id__user_id__username',
        'cat_id__name',
        'cat_id__job',
        'latitude',
        'longitude'
    ]


@admin.register(CatOrigin)
class CatOriginAdmin(admin.ModelAdmin):
    search_fields = [
        'cat_id__user_id__email',
        'cat_id__user_id__username',
        'cat_id__name',
        'cat_id__job',
        'latitude',
        'longitude'
    ]


@admin.register(InterestPoint)
class InterestPointAdmin(admin.ModelAdmin):
    search_fields = [
        'latitude',
        'longitude'
    ]


@admin.register(InteractCat)
class InteractCatAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id__email',
        'user_id__username',
        'cat_id__user_id__email',
        'cat_id__user_id__username',
        'cat_id__name',
        'cat_id__job',
        'is_enabled'
    ]


@admin.register(InteractInterestPoint)
class InteractInterestPointAdmin(admin.ModelAdmin):
    search_fields = [
        'user_id__email',
        'user_id__username',
        'interest_point_id__latitude',
        'interest_point_id__longitude',
        'is_enabled'
    ]
