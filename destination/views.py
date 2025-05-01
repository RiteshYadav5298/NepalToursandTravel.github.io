from django.shortcuts import render

from destination.forms import destination_form
from feedback.models import userfeedback
from .models import destinationplace
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

# def feedbackview(request):
#     if request.method=='POST':
#         form=userfeedbackform(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         else:
#             form=userfeedbackform()
#     form=userfeedbackform()
#     return render(request,'/')


def displayPlaces(request):
    if request.method=='POST':
        form=destination_form(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data['place']
            print(data)
            forms = destinationplace.objects.filter(place=data)
            form=destination_form()
            feedbac = userfeedback.objects.all()
            return render(request,'../templates/index.html',{'rentlink':'/rent','feedbackform':feedbac,'logoutlink':'/logout','forms':forms,'form':form,'loginlink': '/login','hotellink':'/hotel','flightlink':'/flight','homelink':'/home','contactlink':'/contact','currencylink':'/currency','numberlink':'/number','guidelink':'/guide','weatherlink':'/weather','destinationlink':'/destination'})

    feedbac = userfeedback.objects.all()
    form=destination_form()
    return render(request,'../templates/index.html',{'rentlink':'/rent','feedbackform':feedbac,'bookdetaillink':'/allbook','logoutlink':'/logout','form':form,'loginlink': '/login','hotellink':'/hotel','flightlink':'/flight','homelink':'/home','contactlink':'/contact','currencylink':'/currency','numberlink':'/number','guidelink':'/guide','weatherlink':'/weather','destinationlink':'/destination'})
