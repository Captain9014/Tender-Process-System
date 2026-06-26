from django.db import models
from django.conf import settings
from tenderapp.models import Tender


class Bid(models.Model):

    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE
    )

    builder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField()

    duration = models.CharField(
        max_length=100
    )

    proposal = models.TextField()

    is_selected = models.BooleanField(
    default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.proposal