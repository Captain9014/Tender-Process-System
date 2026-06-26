from django.db import models
from django.conf import settings


class Tender(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    budget = models.IntegerField()

    location = models.CharField(max_length=100)

    deadline = models.DateField()

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    STATUS_CHOICES = (
    ('open', 'Open'),
    ('assigned', 'Assigned'),
    ('completed', 'Completed'),
    )

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title