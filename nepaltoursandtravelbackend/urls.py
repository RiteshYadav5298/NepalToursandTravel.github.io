"""nepaltoursandtravelbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from agent.views import veiwguidedata
from airlines.views import ticketing
from booking.views import flightbook
from destination.views import displayPlaces
from hotel.views import RoomDetail, hbook
from payment.views import pay
from rent.views import viewCarDetail
from user.views import data, logins, logouts, bookingDetails


def contact(request):
    return render(request, '../templates/contact.html',
                  {'rentlink':'/rent','bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})


def currency(request):
    return render(request, '../templates/currency.html',
                  {'rentlink':'/rent','bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})


def number(request):
    return render(request, '../templates/number.html',
                  {'rentlink':'/rent','bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})


def weather(request):
    return render(request, '../templates/weather.html',
                  {'rentlink':'/rent','bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})


def destination(request):
    return render(request, '../templates/destination.html',
                  {'rentlink':'/rent','bookdetaillink': '/allbook', 'logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact),
    path('currency/', currency),
    path('number/', number),
    path('guide/', veiwguidedata),
    path('weather/', weather),
    path('destination/', destination),
    path('home/', displayPlaces),
    path('hotel/', RoomDetail),
    path('flight/', ticketing),
    path('login/', logins),
    path('book/<int:id>/', flightbook, name="book"),
    path('payment/<int:id>/<str:method>/', pay, name="payment"),
    path('hotelbook/<int:id>/<str:checkin>/<str:checkout>/', hbook, name="payment"),
    path('userdata/<int:id>/', data, name="user"),
    path('logout/', logouts),
    path('allbook/', bookingDetails),
    path('rent/', viewCarDetail),
    # path('savedata/<int:id>/',savedata, name="usersave"),
    # path('accounts/', include('allauth.urls')),
]
