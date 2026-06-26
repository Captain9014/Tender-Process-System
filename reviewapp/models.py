from django.db import models
from django.conf import settings
from tenderapp.models import Tender


class Review(models.Model):

    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_reviews'
    )

    builder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='builder_reviews'
    )

    rating = models.IntegerField()

    review = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.review