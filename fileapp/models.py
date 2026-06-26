from django.db import models
from tenderapp.models import Tender
from django.conf import settings


class ProjectFile(models.Model):

    tender = models.ForeignKey(
        Tender,
        on_delete=models.CASCADE
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='project_files/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.file.name