from django import forms
from . import models


class DonateForm(forms.ModelForm):
    class Meta:
        model = models.Donate
        fields = "__all__"
