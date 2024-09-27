# create_superuser.py
import os
from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')

if username and password and email:
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print(f"Superuser {username} already exists")
else:
    print("Superuser credentials are not provided in environment variables")
