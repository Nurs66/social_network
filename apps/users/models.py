from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.users.managers import CustomUserManager
from django.utils import timezone


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    last_activity = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('-id',)

    def __str__(self):
        return self.email


