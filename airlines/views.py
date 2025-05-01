from django.shortcuts import render

# Create your views here.
from airlines.forms import ticket_form
from airlines.models import ticket, flight


def ticketing(request):
    if request.method=='POST':
       form = ticket_form(request.POST or None)
       if form.is_valid():
           origin = form.cleaned_data['origin']
           destination = form.cleaned_data['destination']
           data = ticket.objects.get(origin=origin, destination=destination)
           flights = data.ticket_id
           print(flights)
           flight_data = flight.objects.filter(tickets_id=flights)
           print(flight_data)
           return render(request, '../templates/bookflight.html',{'rentlink':'/rent','bookdetaillink':'/allbook','logoutlink':'/logout','form':flight_data,'loginlink': '/login','homelink':'/home','contactlink':'/contact','currencylink':'/currency','numberlink':'/number','guidelink':'/guide','weatherlink':'/weather','destinationlink':'/destination','flightlink':'/flight','hotellink':'/hotel'})
       else:
           form = ticket_form()
    form = ticket_form()
    return render(request, '../templates/flight.html',{'rentlink':'/rent','bookdetaillink':'/allbook','logoutlink':'/logout','form':form,'loginlink': '/login','homelink':'/home','contactlink':'/contact','currencylink':'/currency','numberlink':'/number','guidelink':'/guide','weatherlink':'/weather','destinationlink':'/destination','flightlink':'/flight','hotellink':'/hotel'})
