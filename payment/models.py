from django.db import models

from user.models import UsersData

# Create your models here.
class payments(models.Model):
    select= [('cash','cash'),('E-payment','E-payment')]
    payment_method = models.CharField('Payment method', choices=select, default="Cash", max_length=120)
    price=models.PositiveIntegerField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UsersData, on_delete=models.CASCADE)
