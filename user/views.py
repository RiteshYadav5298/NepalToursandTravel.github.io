from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from user.forms import loginform, useremaiform, userform
from user.models import UsersData, Users
from booking.models import booking
from hotel.models import Booking


# Create your views here.
def logins(request):
    if request.method == 'POST':
        form = loginform(request.POST or None)
        signupform = useremaiform(request.POST or None)
        if signupform.is_valid():
            user = signupform.cleaned_data['email']
            repassw = signupform.cleaned_data['repassword']
            passw = signupform.cleaned_data['password']
            if passw == repassw:
                userr = Users.objects.create_user(email=user, password=passw)
                userr.save()
                idf = Users.objects.get(email=user)
                ida = idf.id
                print(ida)
                return HttpResponseRedirect('/userdata/{}'.format(ida))
            else:
                form = loginform()
                signup = useremaiform()
                return render(request, '../templates/login.html',
                              {'rentlink':'/rent','form': form, 'signup': signup, 'loginlink': '/login', 'hotellink': '/hotel',
                               'flightlink': '/flight',
                               'homelink': '/home',
                               'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                               'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})

        elif form.is_valid():
            user = form.cleaned_data['email']
            passw = form.cleaned_data['password']

            try:

                users = authenticate(username=user, password=passw)

                if users is not None:
                    login(request, users)

                    data = Users.objects.get(email=user)
                    id = data.id
                    p = UsersData.objects.get(useremail_id=id)
                    p_id = p.id
                    return render(request, '../templates/index.html',
                                  {'id': p_id,'rentlink':'/rent','bookdetaillink':'/allbook', 'loginlink': '/login', 'form': form, 'hotellink': '/hotel',
                                   'flightlink': '/flight', 'homelink': '/home',
                                   'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                                   'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})
            except:
                return HttpResponse("error")

    form = loginform()
    signup = useremaiform()
    return render(request, '../templates/login.html',
                  {'form': form,'rentlink':'/rent', 'signup': signup, 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight',
                   'homelink': '/home',
                   'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                   'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})


def data(request, id):
    if request.method == 'POST':
        signup = userform(request.POST or None)
        if signup.is_valid():
            print(signup.cleaned_data['FirstName'])
            fname = signup.cleaned_data['FirstName']
            lname = signup.cleaned_data['LastName']
            age = signup.cleaned_data['age']
            phone = signup.cleaned_data['phone']
            gender = signup.cleaned_data['gender']
            address = signup.cleaned_data['address']
            nationality = signup.cleaned_data['nationality']
            print("av")
            UsersData(FirstName=fname, LastName=lname, age=age, phone=phone, gender=gender, address=address,
                      nationality=nationality, useremail_id=id).save()
            return HttpResponseRedirect('/login')

    form = userform()
    signup = useremaiform()
    return render(request, '../templates/userdata.html',
                  {'rentlink':'/rent','form': form, 'signup': signup, 'loginlink': '/login', 'hotellink': '/hotel',
                   'flightlink': '/flight',
                   'homelink': '/home',
                   'contactlink': '/contact', 'currencylink': '/currency', 'numberlink': '/number',
                   'guidelink': '/guide', 'weatherlink': '/weather', 'destinationlink': '/destination'})


def logouts(request):
    logout(request)
    return HttpResponseRedirect('/login')


def bookingDetails(request):
    if request.user.is_authenticated:
        getuserid = Users.objects.get(email=request.user)
        uid = getuserid.id
        getUsers = UsersData.objects.get(useremail_id=uid)
        userID = getUsers.id
        flightdet = booking.objects.filter(user_id=userID)
        hoteldet = Booking.objects.filter(user_id=userID)
        return render(request, '../templates/allbookings.html',
                      {'rentlink':'/rent','bookdetaillink':'/allbook','form': hoteldet, 'flightform': flightdet, 'logoutlink': '/logout', 'loginlink': '/login',
                       'hotellink': '/hotel',
                       'flightlink': '/flight', 'homelink': '/home', 'contactlink': '/contact',
                       'currencylink': '/currency',
                       'numberlink': '/number', 'guidelink': '/guide', 'weatherlink': '/weather',
                       'destinationlink': '/destination'})
