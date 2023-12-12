from rest_framework.response import Response
from rest_framework import status
from TFF.settings import DB_USER
from core.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
    
class HealthCheckAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):

        if User.objects.filter(username=DB_USER).exists():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
