from django import forms
from .models import Users, UsersData

class userform(forms.ModelForm):
    class Meta:
        model=UsersData
        fields=['FirstName','LastName','age','phone','gender','address','nationality']

class loginform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)

class useremaiform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)