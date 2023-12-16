import math
import random
from rest_framework.views import APIView
from TFF.settings import DROP_CHANCE_CAT, JOB_CHOICES
from core.cat.serializers import CatSerializer
from core.interact.serializers import InteractCatSerializer
from core.models import Cat, CatImage, InteractCat, InteractInterestPoint, InterestPoint
from rest_framework.response import Response
from rest_framework import status
from core.user.serializers import UserDataSerializer
from core.utils import getCatImgAI, getColorClan, uploadImgToCloud
from django.utils import timezone


class InteractWithInterestPointAPIView(APIView):

    def get(self, request):

        interest_id = int(request.GET.get('id', None))
        interest = InterestPoint.objects.get(id=interest_id)

        if InteractInterestPoint.objects.filter(user_id=request.user, interest_point_id=interest).exists():
            return Response({
                "message": "You have already interacted with this point."
            }, status=status.HTTP_400_BAD_REQUEST)       
        else:
            InteractInterestPoint.objects.create(
                interest_point_id=interest,
                user_id=request.user
            )

            gained_food = 0
            cat_instance = None
            result = {
                "gained_food": gained_food,
                "cat": cat_instance
            }
            if random.randrange(0, 101) > DROP_CHANCE_CAT:
                gained_food = random.randrange(4, 10)
                result["gained_food"] = gained_food
                request.user.gain_food(gained_food)
            else:
                jobs = JOB_CHOICES.split(" ")
                job_random = jobs[random.randrange(0, len(jobs))]
                cat_instance = Cat.objects.create(
                    user_id=request.user,
                    job=job_random          
                )
                color = getColorClan(request.user.data.clan_id.name)  
                image_response = getCatImgAI(job_random, color, 1, 0)
                image_ref = CatImage.objects.create(
                    cat_id=cat_instance,
                    seed=image_response["seed"]
                )
                uploadImgToCloud(str(image_ref.image_uuid), image_response["image"])
                result["cat"] = CatSerializer(cat_instance).data
            request.user.gain_exp(1)
            result["user_data"] = UserDataSerializer(request.user.data).data

            return Response(result, status=status.HTTP_200_OK)


class InteractWithCatAPIView(APIView):

    def get(self, request):

        cat_id = int(request.GET.get('id', None))
        food_to_give = int(request.GET.get('food', None))
        cat = Cat.objects.get(id=cat_id)

        if request.user.data.food<food_to_give:
            return Response({
                "message": "You don't have enough food."
            }, status=status.HTTP_400_BAD_REQUEST)

        if InteractCat.objects.filter(cat_id=cat, user_id=request.user).exists():
            interact=InteractCat.objects.get(cat_id=cat, user_id=request.user)
            interact.timestamp = timezone.now()
            interact.save()
        else:
            interact=InteractCat.objects.create(
                cat_id=cat,
                user_id=request.user
            )

        if (food_to_give+interact.given_food)>request.user.data.limite_food:
            return Response({
                "message": "You are trying to exceed the authorized food limit."
            }, status=status.HTTP_400_BAD_REQUEST)

        cat_clan = cat.user_id.data.clan_id
        user_clan = request.user.data.clan_id
        effective_food = food_to_give

        if cat_clan==user_clan:
            if cat_clan.effect_id==1:
                effective_food=effective_food+math.ceil(food_to_give*(10/100))             
            success_nurture = cat.gain_food(effective_food)
            if not success_nurture:
                return Response({
                    "message": "This cat cannot level up because enemy cat territories are still present in the targeted area."
                }, status=status.HTTP_400_BAD_REQUEST)        
        else:
            if cat_clan.effect_id==2:
                effective_food=effective_food-math.ceil(food_to_give*(10/100))
            if user_clan.effect_id==3:
                effective_food=effective_food+math.ceil(food_to_give*(10/100))
            cat.gain_poison_food(effective_food)
        
        interact.given_food = interact.given_food+food_to_give
        interact.save()
        request.user.lose_food(food_to_give)
        request.user.gain_exp(food_to_give)

        return Response({
            "user_data": UserDataSerializer(request.user.data).data,
            "cat": CatSerializer(cat).data,
            "interact": InteractCatSerializer(interact).data
        }, status=status.HTTP_200_OK)


class ResetInterestPointAPIView(APIView):

    def get(self, request):

        if request.user.is_superuser:
            InterestPoint.objects.all().delete()
            interacts_cat = InteractCat.objects.all()
            interacts_cat.update(given_food=0)
            cats = Cat.objects.all()
            for cat in cats:
                cat.randomize_position()

            return Response({
                "message": "Reset successfull."
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Insufficient permissions."
            }, status=status.HTTP_403_FORBIDDEN)
