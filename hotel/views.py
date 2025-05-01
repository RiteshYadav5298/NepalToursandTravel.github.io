
from datetime import datetime
from time import strftime
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy

from user.models import Users
from .models import Room, Booking, Hotel
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
from django.contrib.auth.decorators import login_required

# Create your views here.

def RoomDetail(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            print("add")
            h_name = form.cleaned_data['hotel_name']
            category = form.cleaned_data['room_category']
            hotel = Hotel.objects.get(hotel_name=h_name)
            sdate = datetime.strftime(form.cleaned_data['check_in'],"%Y-%m-%d")
            edate = datetime.strftime(form.cleaned_data['check_out'],"%Y-%m-%d")
            print(edate)
            rooms = hotel.id
            room_list = Room.objects.filter(hotel_id=rooms).filter(category=category)
            return render(request, '../templates/roomdisplay.html',
                          {'rentlink':'/rent','bookdetaillink':'/allbook','form': room_list,'logoutlink':'/logout','checkin':sdate,'checkout':edate,'loginlink': '/login', 'hotellink': '/hotel', 'flightlink': '/flight', 'homelink': '/home',
                           'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                           'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})
        else:
            form = AvailabilityForm()
    form = AvailabilityForm()
    return render(request, '../templates/hotel.html',
                  {'rentlink':'/rent','bookdetaillink':'/allbook','form': form,'logoutlink':'/logout', 'hotellink': '/hotel','loginlink': '/login', 'flightlink': '/flight', 'homelink': '/home',
                   'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                   'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})

@login_required(login_url='/login')
def hbook(request,id,checkin,checkout):
    if request.user.is_authenticated:
        getuserid = Users.objects.get(email=request.user)
        uid = getuserid.id
        Booking(user_id=uid,room_id=id,check_in=checkin,check_out=checkout).save()
        return HttpResponseRedirect('/hotel')
    else:
        return HttpResponseRedirect('/login')
        
    # def post(self, request, *args, **kwargs):
    #     category = self.kwargs.get('category', None)
    #     room_list = Room.objects.filter(category=category)
    #     form = AvailabilityForm(request.POST)
    #
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         available_rooms = []
    #         for room in room_list:
    #             if check_availability(room, data['check_in'], data['check_out']):
    #                 available_rooms.append(room)
    #
    #         if len(available_rooms) > 0:
    #             room = available_rooms[0]
    #             booking = Booking.objects.create(
    #                 user=self.request.user,
    #                 room=room,
    #                 check_in=data['check_in'],
    #                 check_out=data['check_out']
    #             )
    #             booking.save()
    #             return HttpResponse(booking)
    #         else:
    #             return HttpResponse('All of this category of room are booked!!! Try another one')


# class BookingView(FormView):
#     form_class = AvailabilityForm
#     template_name = 'availability_form.html'
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         room_list = Room.objects.filter(category=data['room_category'])
#         available_rooms=[]
#         for room in room_list:
#             if check_availability(room, data['check_in'], data['check_out']):
#                 available_rooms.append(room)
#
#         if len(available_rooms) > 0:
#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user=self.request.user,
#                 room=room,
#                 check_in=data['check_in'],
#                 check_out=data['check_out']
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse('All of this category of room are booked!!! Try another one')


class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('hotel:BookingList')
