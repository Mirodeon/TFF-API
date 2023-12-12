from TFF.settings import DB_EMAIL, DB_PASSWORD, DB_USER
from core.user.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username=DB_USER).exists():
            User.objects.create_superuser(
                username=DB_USER,
                email=DB_EMAIL,
                password=DB_PASSWORD
            )
        print('Superuser has been created.')