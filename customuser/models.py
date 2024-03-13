from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


# Create your models here.
Role_Choices = (('user', 'user'),
                ('vendor', 'vendor'))


# added

class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )
        return user


class User(AbstractUser):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=Role_Choices, max_length=200)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    # is_confirmed = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    # user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    # class Meta:
    #     ordering = ("email")
