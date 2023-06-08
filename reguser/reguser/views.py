from django.shortcuts import render
from reguser.models import Userreg
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import redirect

def Userregistration(request):
    if request.user.is_authenticated:
        return redirect('../../')
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('password') and request.POST.get('gender') and request.POST.get('Re-Password'): 
            saverecord = Userreg()
            saverecord.username = request.POST.get('username')
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            repassword = request.POST.get('Re-Password')
            saverecord.gender = request.POST.get('gender')
            if repassword != saverecord.password:
                messages.error(request, 'The passwords are not matched')
                return render(request,'registration/create_user.html')
            try:
                saveuser = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), password=request.POST.get('password'))
                saveuser.save()
                saverecord.save()
                messages.success(request, "New User Registration Details Saved Successfully..!")
                return render(request,'registration/create_user.html')
            except IntegrityError:
                messages.error(request, 'The User is not defined')
                return render(request,'registration/create_user.html')
        else:
            messages.success(request, "")
            return render(request, 'registration/create_user.html')
    else:
        messages.success(request, "")
        return render(request,'registration/create_user.html')

def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('../../')
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') : 
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, "Successfully find the user")
                # return render(request,'registration/login.html')
                return render(request,'home.html')
            else:
                messages.error(request, "Invalid informations")
                return render(request,'registration/login.html')
    messages.success(request, "")
    return render(request,'registration/login.html')