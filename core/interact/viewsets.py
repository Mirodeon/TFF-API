import random
from rest_framework.views import APIView
from core.models import Cat, CatImage, InteractInterestPoint, InterestPoint
from rest_framework.response import Response
from rest_framework import status

class InteractWithInterestPoint(APIView):

    def get(self, request):

        interest_id = int(request.GET.get('id', None))
        interest = InterestPoint.objects.get(id=interest_id)

        if InteractInterestPoint.objects.filter(user_id=request.user, interest_point_id=interest).exists():

            return Response({
                "message": "You have already interacted with this point."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        else:

            if random.randrange(1, 100) > 5:
                gained_food = random.randrange(4, 9)
                request.user.gain_food(gained_food)
            else:
                cat_instance = Cat.objects.create(
                    user_id=request.user,
                    clan_id=request.user.data.clan_id,
                    name="Test",
                    job="Knight"          
                )

                CatImage.objects.create(
                    cat_id=cat_instance,
                    seed=101
                )
            request.user.gain_exp(1)
        
        return





class InteractWithCat(APIView):

    def get(self, request):

        cat_id = int(request.GET.get('id', None))
        food_given = int(request.GET.get('food', None))

        request.user.gain_exp(food_given)
