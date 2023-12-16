import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from django.utils import timezone
import os
from TFF.settings import LVL_MAX_CAT, LVL_MAX_USER, MIN_RADIUS_CAT, RADIUS_VIEW
from core.utils import distanceBetweenGPSPoint, getCatImgAI, getClanChoices, getColorClan, getJobChoices, uploadImgToCloud


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have an username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=24, unique=True)
    email = models.EmailField(
        db_index=True, unique=True,  null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def gain_exp(self, exp):     
        try:
            user_data = self.data
        except UserData.DoesNotExist:
            return 
        if user_data.limite_exp <= (user_data.exp+exp):
            if user_data.lvl<LVL_MAX_USER:
                user_data.exp = user_data.exp+exp-user_data.limite_exp
                user_data.limite_exp = ((user_data.lvl*(user_data.lvl+1))/2)+5
                user_data.lvl = user_data.lvl+1
                user_data.limite_food = user_data.lvl*2+5
            else:
                user_data.exp=user_data.limite_exp
        else:
            user_data.exp = user_data.exp+exp
        user_data.save()

    def gain_food(self, food):     
        try:
            user_data = self.data
        except UserData.DoesNotExist:
            return 
        user_data.food = user_data.food+food
        user_data.save()

    def __str__(self):
        return f"{self.pk}: {self.email}"


class Clan(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=24, choices=getClanChoices())
    effect_id = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.pk}: {self.name}"


class UserData(models.Model):
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, related_name='data')
    clan_id = models.ForeignKey('Clan', on_delete=models.CASCADE, related_name='users_data')
    food = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    limite_food = models.IntegerField(validators=[MinValueValidator(5)], default=5)
    lvl = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    exp = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    limite_exp = models.IntegerField(validators=[MinValueValidator(5)], default=5)

    def __str__(self):
        return f"{self.user_id}"
    

class UserImage(models.Model):
    user_data_id = models.OneToOneField('UserData', on_delete=models.CASCADE, related_name='image')
    image_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    seed = models.IntegerField()

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/{os.getenv('CLOUDINARY_CLOUD_NAME')}/{self.image_uuid}.png"
        )

    def __str__(self):
        return f"{self.user_data_id} - {self.image_url}"


class Cat(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=24, default="Unknown")
    job = models.CharField(db_index=True, max_length=24, choices=getJobChoices())
    lvl = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    exp = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    limite_exp = models.IntegerField(validators=[MinValueValidator(50)], default=50)
    timestamp = models.DateTimeField(default=timezone.now)
    alive = models.BooleanField(default=True)
    radius = models.IntegerField(validators=[MinValueValidator(MIN_RADIUS_CAT)], default=MIN_RADIUS_CAT)

    def is_on_map(self):
        return CatOrigin.objects.filter(cat_id=self).exists()

    def is_in_radius(self, lat, lon):
        try:
            origin = self.origin
        except CatOrigin.DoesNotExist:
            return False
        return origin.is_in_radius(lat, lon)
    
    def is_same_clan(self, origin):
        return self.user_id.data.clan_id == origin.cat_id.user_id.data.clan_id
    
    def can_lvl_up(self):
        try:
            origin = self.origin
        except CatOrigin.DoesNotExist:
            return False       
        for cat_origin in CatOrigin.objects.all():
            if not self.is_same_clan(cat_origin) and cat_origin.cat_id.alive:
                distance_between = distanceBetweenGPSPoint(
                    cat_origin.latitude, 
                    origin.latitude, 
                    cat_origin.longitude,
                    origin.longitude
                )
                if distance_between<(self.radius+cat_origin.cat_id.radius):
                    return False
        return True
    
    def update_img(self):
        color = getColorClan(self.user_id.data.clan_id.name) 
        image_response = getCatImgAI(self.job, color, self.lvl, self.image.seed)
        uploadImgToCloud(str(self.image.image_uuid), image_response["image"])
    
    def gain_food(self, food):
        success = True
        if self.limite_exp <= (self.exp+food):
            success = self.can_lvl_up()
            if success:
                if self.lvl<LVL_MAX_CAT:
                    self.exp = self.exp+food-self.limite_exp
                    self.limite_exp = 50*pow(2, self.lvl)
                    self.radius = MIN_RADIUS_CAT*pow(2, self.lvl)
                    self.lvl = self.lvl+1
                    self.update_img()
                else:
                    self.exp=self.limite_exp
        else:
            self.exp = self.exp+food
        self.save()
        return success

    def gain_poison_food(self, food):
        if 0 > (self.exp-food):
            if self.lvl-1 == 0:
                self.exp = 0
                self.alive = False
            else:
                self.lvl = self.lvl-1
                self.limite_exp = 50*pow(2, self.lvl-1)
                self.exp = self.limite_exp-food+self.exp
                self.update_img()          
        else:
            self.exp = self.exp-food
        self.save()

    def hasInteractWith(self, user):
        try:
            interact = InteractCat.objects.get(user_id=user, cat_id=self)
        except InteractCat.DoesNotExist:
            return False
        return True

    def __str__(self):
        return f"{self.pk}: {self.name} from {self.user_id}"


class CatImage(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='image')
    image_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    seed = models.IntegerField(default=0)

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/{os.getenv('CLOUDINARY_CLOUD_NAME')}/{self.image_uuid}.png"
        )

    def __str__(self):
        return f"{self.cat_id}, image id: {self.image_uuid}"


class CatOrigin(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='origin')
    longitude = models.FloatField()
    latitude = models.FloatField()
    
    def is_in_radius(self, lat, lon):
        return RADIUS_VIEW >= distanceBetweenGPSPoint(self.latitude, lat, self.longitude, lon)

    def __str__(self):
        return f"{self.cat_id}"
    

class CatPosition(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='position')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def is_in_radius(self, lat, lon):
        return RADIUS_VIEW >= distanceBetweenGPSPoint(self.latitude, lat, self.longitude, lon)

    def __str__(self):
        return f"{self.cat_id}"


class InterestPoint(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    # 0.02 range random

    def is_in_radius(self, lat, lon):
        return RADIUS_VIEW >= distanceBetweenGPSPoint(self.latitude, lat, self.longitude, lon)

    def __str__(self):
        return f"[{self.pk}: {self.latitude}, {self.longitude}]"


class InteractCat(models.Model):
    cat_id = models.ForeignKey('Cat', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    given_food = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.user_id} interact with {self.cat_id}"


class InteractInterestPoint(models.Model):
    interest_point_id = models.ForeignKey(
        'InterestPoint', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_id} interact with {self.interest_point_id}"
