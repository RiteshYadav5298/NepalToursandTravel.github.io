
from django.db import models
from airlines.models import flight

from user.models import UsersData

# Create your models here.
class booking(models.Model):
    user = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    flight_Date = models.DateTimeField()
    flightdet = models.ForeignKey(flight, on_delete=models.CASCADE)
