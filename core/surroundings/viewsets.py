from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import InterestPoint, Cat
from core.surroundings.serializers import CatWithInteractSerializer, InterestPointWithInteractSerializer
from django.db.models import Func, F


class SurroundingsAPIView(APIView):

    def get(self, request):

        lat = float(request.GET.get('lat', None))
        lon = float(request.GET.get('lon', None))

        interest_points = InterestPoint.objects.annotate(
            abs_calculation=Func(F('latitude') - lat, function='ABS')
            + Func(F('longitude') - lon, function='ABS')
        ).filter(abs_calculation__lt=0.05)

        cats = Cat.objects.annotate(
            abs_calculation=Func(F('position__latitude') - lat, function='ABS')
            + Func(F('position__longitude') - lon, function='ABS')
        ).filter(abs_calculation__lt=0.05)

        data = {
            "interest_points": InterestPointWithInteractSerializer(interest_points, many=True, context={'request': request}).data,
            "cats": CatWithInteractSerializer(cats, many=True, context={'request': request}).data
        }

        return Response(data)