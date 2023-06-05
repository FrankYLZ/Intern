from django.shortcuts import render
from reguser.models import Userreg
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from reguser.forms import CustomUserCreationForm

def Userregistration(request):
    if request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('password') and request.POST.get('gender'): 
            saverecord = Userreg()
            saverecord.username = request.POST.get('username')
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            form.save()
            user = authenticate(request, user)
            login(request, user)
            messages.success(request, "New User Registration Details Saved Successfully..!")
            return render(request,'registration/create_user.html')
        else:
            return render(request, 'registration/create_user.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request,'registration/create_user.html', {'form':form})

def UserLogin(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'): 
            # saverecord = Userreg()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                render(request,'')
            return render(request,'registration/login.html')
    else:
        return render(request,'registration/login.html')