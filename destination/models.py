from django.db import models

class destinationplace(models.Model):
    places=(('Pokhara','Pokhara'),('Janakpur','Janakpur'),('Kathmandu','Kathmandu'),('Lumbini','Lumbini'))
    place = models.CharField(max_length=120, choices=places)
    description = models.TextField()
