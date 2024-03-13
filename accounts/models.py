from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
