from django.shortcuts import render
from .models import agent
# Create your views here.
def veiwguidedata(request):
    data = agent.objects.all()
    return render(request,'../templates/guide.html',{'form':data,'rentlink':'/rent','bookdetaillink':'/allbook','logoutlink':'/logout','loginlink': '/login','hotellink':'/hotel','flightlink':'/flight','homelink':'/home','contactlink':'/contact','currencylink':'/currency','numberlink':'/number','guidelink':'/guide','weatherlink':'/weather','destinationlink':'/destination'})
