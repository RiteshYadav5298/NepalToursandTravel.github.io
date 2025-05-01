from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


# Create your models here.
class Hotel(models.Model):
    hotel_name = (
        ('Hotel Average', 'Hotel Average'),
        ('Hotel Plaza', 'Hotel Plaza'),
        ('Hotel Angel', 'Hotel Angel'),
        ('Hotel GreenOrchid', 'Hotel GreenOrchid'),
    )
    hotel_name = models.CharField(max_length=120,choices=hotel_name)

    def __str__(self):
        return f'{self.hotel_name}'


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,default=1)
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    price = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
        return reverse_lazy('hotel:CancelBookingView', args=[self.pk, ])



