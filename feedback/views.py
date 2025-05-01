from django.shortcuts import render

from feedback.forms import userfeedbackform
from .models import userfeedback
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

def feedbackview(request):
    if request.method=='POST':
        form=userfeedbackform(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            form=userfeedbackform()
    form=userfeedbackform()
    return render(request,'/')


def displayfeedback(request):
    data=userfeedback.objects.all()
    return render(request,'/',{'form':data})