from django import forms
from .models import GarageSell

class GarageForm(forms.ModelForm):
    class Meta:
        model=GarageSell
        fields='__all__'