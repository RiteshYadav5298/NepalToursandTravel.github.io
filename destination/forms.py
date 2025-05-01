from django import forms
from .models import destinationplace

class destination_form(forms.ModelForm):
    class Meta:
        model = destinationplace
        fields = ['place']