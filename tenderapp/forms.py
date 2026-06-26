from django import forms
from .models import Tender


class TenderForm(forms.ModelForm):

    class Meta:
        model = Tender

        fields = [
            'title',
            'description',
            'budget',
            'location',
            'deadline'
        ]