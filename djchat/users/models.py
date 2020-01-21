from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    tagline = models.TextField(
        verbose_name="description",
        max_length=1024,
        default='',
        blank=True)
