#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser automatically
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'haritha@gtec'
email = 'harithacholayil01@gmail.com'
password = 'hari@gtec1974'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created')
else:
    print('Superuser already exists')
" | python manage.py shell

# Collect static files
python manage.py collectstatic --no-input
