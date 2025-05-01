from django.db import models

# Create your models here.
class carRent(models.Model):
    StoreName=models.CharField(max_length=150)
    OwnerName=models.CharField(max_length=120)
    Phone = models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=120)
