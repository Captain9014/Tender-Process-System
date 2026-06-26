from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):

    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    company_name = models.CharField(
        max_length=100,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    about = models.TextField(
        blank=True
    )

    ROLE_CHOICES = (
        ('client', 'Client'),
        ('builder', 'Builder'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='builder'
    )


class BlockBuilder(models.Model):

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_by_client'
    )

    builder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_builder'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.client} blocked {self.builder}"


class UserBlock(models.Model):

    blocked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_users'
    )

    blocked_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blocked_by_users'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.blocked_by} blocked {self.blocked_user}"
    

