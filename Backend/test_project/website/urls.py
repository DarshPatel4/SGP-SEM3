from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'), 
    path('secondpage.html', views.secondpage , name = 'secondpage')
    
]
