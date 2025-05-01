from django.shortcuts import render
from .models import carRent


# Create your views here.

def viewCarDetail(request):
    data = carRent.objects.all()
    return render(request, '../templates/rent.html',
                  {'form': data, 'bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login',
                   'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})
