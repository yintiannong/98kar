import os

import django

from django.test import TestCase
# Create your tests here.


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.steup()
from zuoye_app.models import User
User

