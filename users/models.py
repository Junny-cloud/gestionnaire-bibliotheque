from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings


# Create your models here.
from config import settings

class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Téléphone")
    profession = models.CharField(max_length=100, null=True, blank=True, verbose_name="profession")
    
    
    USERNAME_FIELD = "username"  # e.g: "username", "email"
    EMAIL_FIELD = "email"
    
    class Meta:
        verbose_name = "Bibliothécaire"
        verbose_name_plural = "Bibliothécaires"
        ordering = ['-id']

    def __str__(self):
        return f"{self.get_full_name()}"
    