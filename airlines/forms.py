from django import forms
from .models import ticket

class ticket_form(forms.ModelForm):
    adult = forms.IntegerField()
    class Meta:
        model = ticket
        fields = ['origin', 'destination','departure_date','adult']

        