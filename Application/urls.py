from django.urls import path
from . import views

urlpatterns = [

    path("newyear", views.newyear, name="year"),
    path("mbote", views.mbote, name="ttt"),
    path("mobilis", views.mobilis, name="mobilis"),
    path("", views.mobilis, name="mobilis"),
    path("", views.msg, name="msg"),
    path("home", views.home, name="home"),
]