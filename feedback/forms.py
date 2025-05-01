from django import forms
from .models import userfeedback

class userfeedbackform(forms.ModelForm):
    class Meta:
        model=userfeedback
        fields='__all__'