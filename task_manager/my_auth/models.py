from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class TaskManagerUser(AbstractUser):

    bio = models.TextField(blank=True)



