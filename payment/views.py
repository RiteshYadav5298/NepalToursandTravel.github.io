import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from airlines.models import flight
from booking.models import booking
# Create your views here.
from payment.forms import paymentform
from payment.models import payments
from user.models import Users


@login_required(login_url='/login')
def pay(request, id, method):
    if request.user.is_authenticated:
        getuserid = Users.objects.get(email=request.user)
        uid = getuserid.id
        f_id = flight.objects.get(id=id)
        price = f_id.ticket_price
        date = datetime.datetime.combine(f_id.flight_date, f_id.flight_time)
        booking(user_id=uid, flight_Date=date, flightdet_id=id).save()
        if method == 'E-Payment':
            payments(payment_method=method, price=price, user_id=uid, is_paid=True).save()
        else:
            payments(payment_method=method, price=price, user_id=uid).save()
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/login')


def displaypay(request):
    data = payments.objects.all()
    return render(request, '/', {'form': data})
