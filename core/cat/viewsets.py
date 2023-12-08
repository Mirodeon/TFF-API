from rest_framework import viewsets
from core.cat.serializers import CatSerializer
from rest_framework import filters
from core.models import Cat, CatOrigin, CatPosition
from rest_framework.response import Response
from rest_framework import status

from core.utils import distanceBetweenGPSPoint, generatePointWithinRadius


class CatOnMapFromUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self, request):
        cats = [ cat for cat in Cat.objects.filter(user_id=request.user) if cat.is_on_map() ]
        return Response({CatSerializer(cats, many=True).data}, status=status.HTTP_200_OK)
    
    
class CatInBagFromUserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self, request):
        cats = [ cat for cat in Cat.objects.filter(user_id=request.user) if not cat.is_on_map() ]
        return Response({CatSerializer(cats, many=True).data}, status=status.HTTP_200_OK)
    

class CatDropViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']

    def create(self, request):
        cat_id = request.data['cat_id']
        name = request.data['name']
        lat = request.data['latitude']
        lon = request.data['longitude']
        
        cat_instance = Cat.objects.get(id=cat_id)
        can_be_drop = True
        for cat_origin in CatOrigin.objects.all():
            distance_between = distanceBetweenGPSPoint(
                cat_origin.latitude, 
                lat, 
                cat_origin.longitude,
                lon
            )
            if distance_between<(cat_instance.radius+cat_origin.cat_id.radius):
                can_be_drop = False
                break

        if can_be_drop and cat_instance.user_id==request.user:
            cat_instance.name = name
            CatOrigin.objects.create(
                cat_id=cat_instance,
                longitude=lon,
                latitude=lat
            )
            randomPoint = generatePointWithinRadius(lat, lon, cat_instance.radius)
            CatPosition.objects.create(
                cat_id=cat_instance,
                longitude=randomPoint['lonigtude'],
                latitude=randomPoint['latitude']
            )
            cat_instance.save()
            return Response({CatSerializer(cat_instance).data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "This cat cannot be placed in the designated area"},
                status=status.HTTP_400_BAD_REQUEST
            )
