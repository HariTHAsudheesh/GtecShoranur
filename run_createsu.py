import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gtecsite.settings")

django.setup()

from main.management.commands.createsu import run

run()
