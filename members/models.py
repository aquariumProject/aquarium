from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# auth_user의 나머지 필드를 그대로 사용하고 동작하되 nickname 필드를 추가함
class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=False, null=False)