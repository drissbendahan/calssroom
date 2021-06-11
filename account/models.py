from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

