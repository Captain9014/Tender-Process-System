from django import forms
from .models import ProjectFile


class FileUploadForm(forms.ModelForm):

    class Meta:

        model = ProjectFile

        fields = ['file']