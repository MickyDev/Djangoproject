from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

#def newyear(request):
#    return HttpResponse("New-year")


def newyear(request):
     now = datetime.datetime.now()
     return render(request, "index.html",{
         "new": now.month == 1 and now.day == 1
     })



