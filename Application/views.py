from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newyear(request):
    return render(request, "New-year")

def home(request):
    return render(request, "home.html")


def mbote(request):
    return HttpResponse("Hi there!!")

def mobilis(request):
    return HttpResponse("This is E-MOBILIS!!!!")

def msg(request):
    return HttpResponse("This is the MESSAGE!!!!")