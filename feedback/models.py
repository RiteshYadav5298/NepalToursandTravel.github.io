from django.db import models
from user.models import UsersData
# Create your models here.
class userfeedback(models.Model):
    user = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    message = models.CharField(max_length=130)
