from django.db import models
from django.conf import settings
from tenderapp.models import Tender


class Message(models.Model):

    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.text