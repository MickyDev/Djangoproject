from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime



# Create your views here.

# def christmas(request):
#     template = loader.get_template("xmas.html")
#     return HttpResponse(template.render())

# def christmas(request):
#     current_date = datetime.date.today()
#     "show" : current_date.month == 4 and current_date.day == 4
#
#     return render(request, "xmas.html")



def christmas(request):
    today = datetime.date.today()
    return render(request, "xmas.html", {
        "show": today.month == 12 and today.day == 25
     })