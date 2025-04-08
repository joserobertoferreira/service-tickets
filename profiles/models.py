from django.db import models

from accounts.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
