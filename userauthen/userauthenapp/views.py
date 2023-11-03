from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Information
# Name : Imtiaz Adar
# Project : User Authentication And Adding Users
# Language : Python
# Framework : Django
# Phone : 01778767775, 01979777379
# Email : imtiazadarofficial@gmail.com

def HomePage(request):
    return render(request, 'index.html')

def AddInformation(request):
    if request.method == 'POST':
        add_info = Information()
        fullname = request.POST.get('fullname')
        age = request.POST.get('age')
        current_location = request.POST.get('current_location')
        hometown_location = request.POST.get('hometown_location')
        hobby = request.POST.get('hobby')
        experience = request.POST.get('experience')
        add_info.fullname = fullname
        add_info.age = age
        add_info.current_location = current_location
        add_info.hometown_location = hometown_location
        add_info.hobby = hobby
        add_info.experience = experience
        add_info.save()
        messages.success(request, ('Informations Added Successfully !'))
        return redirect('showinfo')
    return render(request, 'addinformation.html', {})

def ShowInformation(request):
    whole_info = Information.objects.all()
    return render(request, 'showinfo.html', {'whole_info': whole_info})

def Login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, (f'Congratulation {user.first_name} {user.last_name}, You have been logged in !'))
                    return redirect('index')
                else:
                    return HttpResponse('<h1>User is not active</h1>')
            else:
                return HttpResponse('<h1>Login failed...</h1>')
    else:
        login_form = LoginForm()
            
    return render(request, 'login.html', {'login_form': login_form})

def Register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Congratulations! Registered Successfully! '))
            return redirect('login')
    else:
        user_form = RegisterForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def Logout(request):
    logout(request)
    messages.success(request, ('Logged Out Successfully !'))
    return redirect('login')