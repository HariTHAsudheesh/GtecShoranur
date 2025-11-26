from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "haritha@gtec"
        password = "hari@gtec1974"
        email = "harithacholayil01@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password, email=email)
            print("Superuser created!")
        else:
            print("Superuser already exists.")
