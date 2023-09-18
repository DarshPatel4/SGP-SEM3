from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'index.html');

def secondpage(request):
    return render(request , 'secondpage.html')