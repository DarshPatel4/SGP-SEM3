from django.shortcuts import render
from .models import car
# Create your views here.

def index(request):
    cars = car.objects.all()
    return render(request, "index.html " , {'cars' : cars})

def secondpage(request):
    return render(request , "secondpage.html")