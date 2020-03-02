from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.
class Role(models.Model):
    PLAYER = 1
    COACH = 2
    ANALYST = 3
    MANAGER = 4 
    ADMIN = 5
    ROLE_CHOICES = (
        (PLAYER, 'player'),
        (COACH, 'coach'),
        (ANALYST, 'analyst'),
        (MANAGER, 'manager'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    role_name = models.CharField(max_length=255, default='DEFAULT VALUE')

    def __str__(self):
        return self.get_id_display()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_ ('email_address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    roles = models.ManyToManyField(Role)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
       return self.email

