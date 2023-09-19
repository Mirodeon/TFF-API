from rest_framework import permissions
from TFF.settings import API_KEY_CUSTOM_HEADER, SECRET_KEY


class HasAPIKey(permissions.BasePermission):

    message = "The given API key doesn't match."

    def has_permission(self, request, view):

        try:
            return request.META[API_KEY_CUSTOM_HEADER] == SECRET_KEY
        except:
            return False
