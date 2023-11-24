import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from django.utils import timezone
import os


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

    def __str__(self):
        return f"{self.email}"


class Clan(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=24)
    effect_id = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return f"{self.name}"


class UserData(models.Model):
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, related_name='data')
    clan_id = models.ForeignKey('Clan', on_delete=models.CASCADE, related_name='users_data')
    food = models.IntegerField(validators=[MinValueValidator(0)], default=0)
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
            f"https://res.cloudinary.com/{os.getenv('CLOUDINARY_CLOUD_NAME')}/{self.image_uuid}"
        )

    def __str__(self):
        return f"{self.user_data_id}"


class UserPosition(models.Model):
    user_id = models.OneToOneField('User', on_delete=models.CASCADE, related_name='position')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.user_id}"


class Cat(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(db_index=True, max_length=24)
    job = models.CharField(db_index=True, max_length=24)
    lvl = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    exp = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} from {self.user_id}"


class CatImage(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='image')
    image_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    seed = models.IntegerField()

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/{os.getenv('CLOUDINARY_CLOUD_NAME')}/{self.image_uuid}"
        )

    def __str__(self):
        return f"{self.cat_id}"


class CatOrigin(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='origin')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.cat_id}"
    

class CatPosition(models.Model):
    cat_id = models.OneToOneField('Cat', on_delete=models.CASCADE, related_name='position')
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.cat_id}"


class InterestPoint(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    # 0.02 range random

    def __str__(self):
        return f"[{self.latitude}, {self.longitude}]"


class InteractCat(models.Model):
    cat_id = models.ForeignKey('Cat', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_id} interact with {self.cat_id}"


class InteractInterestPoint(models.Model):
    interest_point_id = models.ForeignKey(
        'InterestPoint', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_id} interact with {self.interest_point_id}"
