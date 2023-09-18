from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        
        user = auth.authenticate(username = username , password = password)
        
        if user is not None:
            auth.login(request , user)
            return redirect('/')
        else:
            messages.info(request , 'invalid credenrials')
            return redirect('login')
    else:
        return render(request , 'login.html')

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        email = request.POST['Email']
        if(password1 == password2):
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save(),
                print('user created')
                return redirect('login')
        
        elif password1 != password2:
            print('Password Not Matching')
            return redirect('register')
        else:
            return redirect('login')   
            
        
    else:
        return render(request , 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
