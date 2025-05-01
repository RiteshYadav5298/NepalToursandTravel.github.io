from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView #BookingView,

app_name = 'hotel'



urlpatterns=[
    path('room_list/', RoomListView, name='RoomListView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    #path('book/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
]