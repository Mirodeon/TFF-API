from rest_framework.response import Response
from rest_framework.views import APIView
from TFF.settings import POINT_IN_RADIUS, RADIUS_VIEW
from core.models import InterestPoint, Cat
from core.surroundings.serializers import CatWithInteractSerializer, InterestPointWithInteractSerializer
from core.utils import generatePointWithinRadius
from rest_framework import status


class SurroundingsAPIView(APIView):

    def get(self, request):

        lat = float(request.GET.get('lat', None))
        lon = float(request.GET.get('lon', None))

        interest_points = [ point for point in InterestPoint.objects.all() if point.is_in_radius(lat, lon) ]

        if len(interest_points) < POINT_IN_RADIUS:
            print(len(interest_points))
            for i in range(POINT_IN_RADIUS - len(interest_points)):
                generated_point = generatePointWithinRadius(lat, lon, RADIUS_VIEW)
                point = InterestPoint.objects.create(
                    latitude=generated_point['latitude'],
                    longitude=generated_point['longitude']
                )
                interest_points.append(point)

        cats = [ cat for cat in Cat.objects.all() if cat.is_in_radius(lat, lon) ]

        data = {
            "interest_points": InterestPointWithInteractSerializer(interest_points, many=True, context={'request': request}).data,
            "cats": CatWithInteractSerializer(cats, many=True, context={'request': request}).data
        }

        return Response(data, status=status.HTTP_200_OK)