from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    ) # symmetrical=False 일촌 관계가 아닌 팔로우 관계

    
