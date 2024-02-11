
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def login_home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user),
            return redirect('appay_main')

    return render(request, 'LogReg/login.html')


def Next(request):
    return render(request, 'LogReg/next.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        data = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password = password1)
        data.save()
        return redirect('login_main')
    return render(request, 'LogReg/register.html')
