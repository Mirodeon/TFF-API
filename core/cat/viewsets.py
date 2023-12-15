from core.cat.serializers import CatSerializer
from rest_framework.views import APIView
from rest_framework import filters
from core.models import Cat, CatOrigin, CatPosition
from rest_framework.response import Response
from rest_framework import status
from core.surroundings.serializers import CatWithAllInteractSerializer, CatWithInteractSerializer
from core.utils import distanceBetweenGPSPoint, generatePointWithinRadius
from rest_framework import viewsets


class CatOnMapFromUserAPIView(APIView):

    def get(self, request):
        cats = [ cat for cat in Cat.objects.filter(user_id=request.user) if cat.is_on_map() ]
        return Response({"cats": CatWithAllInteractSerializer(cats, many=True).data}, status=status.HTTP_200_OK)
    
    
class CatInBagFromUserAPIView(APIView):

    def get(self, request):
        cats = [ cat for cat in Cat.objects.filter(user_id=request.user) if not cat.is_on_map() ]
        return Response({"cats": CatSerializer(cats, many=True).data}, status=status.HTTP_200_OK)
    

class CatDropAPIView(APIView):

    def post(self, request):
        cat_id = request.data['cat_id']
        name = request.data['name']
        lat = float(request.data['latitude'])
        lon = float(request.data['longitude'])
        
        cat_instance = Cat.objects.get(id=cat_id)
        can_be_drop = True
        for cat_origin in CatOrigin.objects.all():
            if not cat_origin.cat_id.user_id==request.user:
                distance_between = distanceBetweenGPSPoint(
                    cat_origin.latitude, 
                    lat, 
                    cat_origin.longitude,
                    lon
                )
                if distance_between<(cat_instance.radius+cat_origin.cat_id.radius):
                    can_be_drop = False
                    break

        if can_be_drop:
            cat_instance.name = name
            CatOrigin.objects.create(
                cat_id=cat_instance,
                longitude=lon,
                latitude=lat
            )
            randomPoint = generatePointWithinRadius(lat, lon, cat_instance.radius)
            CatPosition.objects.create(
                cat_id=cat_instance,
                longitude=randomPoint['longitude'],
                latitude=randomPoint['latitude']
            )
            cat_instance.save()
            return Response({"cat": CatSerializer(cat_instance).data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "This cat cannot be placed in the designated area"},
                status=status.HTTP_400_BAD_REQUEST
            )


class CatViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']
    serializer_class = CatWithInteractSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):

        return Cat.objects.all()

    def get_object_or_404(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = Cat.objects.get(id=lookup_field_value)

        return obj