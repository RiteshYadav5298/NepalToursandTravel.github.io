from django.db import models
from user.models import Users

# Create your models here.
class agent(models.Model):
    agentsnames = models.CharField(max_length=120)
    agentsContact = models.IntegerField()
    agentsAddress = models.CharField(max_length=200)
    agentEmail = models.EmailField()
    agentPrice = models.PositiveIntegerField()

