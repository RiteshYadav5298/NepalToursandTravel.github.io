from django.shortcuts import render

from airlines.models import flight


# Create your views here.
def flightbook(request, id):
    f_id = flight.objects.filter(id=id)
    return render(request, '../templates/paymentpage.html',
                  {'form': f_id,'bookdetaillink':'/allbook', 'rentlink':'/rent','logoutlink': '/logout', 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact', 'currencylink': '/currency',
                   'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                   'destinationlink': '/destination'})
