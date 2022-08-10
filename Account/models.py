from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    pass
'''
user_roles = (
    (1, 'admin'),
    (2, 'user')
)
user_type = models.PositiveSmallIntegerField(choices= user_roles, null = True, blank = True)
'''