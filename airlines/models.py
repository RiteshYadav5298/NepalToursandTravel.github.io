from this import d
from django.db import models

# Create your models here.
class ticket(models.Model):
    ticket_id = models.PositiveSmallIntegerField(primary_key=True, default=1)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    departure_date = models.DateField()
    


class flight(models.Model):
    tickets = models.ForeignKey(ticket, on_delete=models.CASCADE)
    flight_name = models.CharField(max_length=150)
    flight_date = models.DateField()
    flight_time = models.TimeField()
    flight_number = models.CharField(max_length=50)
    seat_number = models.PositiveIntegerField()
    ticket_price = models.PositiveIntegerField()