from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        if User.objects.filter(email = email).exists():
            messages.info(request, 'Email already exists!')
            return redirect('login')
        elif User.objects.filter(username = username).exists():
            messages.info(request, 'Username already exists!')
            return redirect('login')
        else:
            user = User.objects.create_user(username = username, email = email, password = password, )
            user.save();
            return redirect('signin')
    else:
        return render(request, 'login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
def signout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')
