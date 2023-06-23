from django.shortcuts import render
from reguser.models import Userreg
from django.contrib import messages
from django.contrib.auth import login, authenticate, views
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
                return redirect("../../")
            else:
                messages.error(request, "Invalid informations")
                return render(request,'registration/login.html')
    messages.success(request, "")
    return render(request,'registration/login.html')


def PasswordReset(request, *args, **kwargs):
    # temp = {'error': 0}
    # context = {**temp, **kwargs}
    context = {'error1': 0, 'error2':0, 'error3': 0}
    if request.method == 'POST':
        if request.POST.get('new_password1') and request.POST.get('new_password2') and request.POST.get('old_password'):
            pass1 = request.POST['new_password1']
            pass2 = request.POST['new_password2']
            oldpass = request.POST['old_password']
            if pass1 != pass2:
                context['error1'] = 1
                return render(request,'registration/password_exists_reset.html', context)
            user = User.objects.get(username=request.user.username)
            usersql = Userreg.objects.get(username=request.user.username)
            if oldpass == pass1:
                context['error3'] = 1
                return render(request,'registration/password_exists_reset.html', context)
            if usersql.password != oldpass:
                context['error2'] = 1
                return render(request,'registration/password_exists_reset.html', context)
            user.set_password(pass1)
            user.save()
            usersql.password = pass1
            usersql.save()
            return render(request,'registration/password_reset_complete.html')
    # validlink = True
    return render(request,'registration/password_exists_reset.html', context)

def PasswordForgot(request, *args, **kwargs):
    # temp = {'error': 0}
    # context = {**temp, **kwargs}
    context = {'error': 0}
    if request.method == 'POST':
        if request.POST.get('new_password1') and request.POST.get('new_password2') and request.POST.get('email'):
            pass1 = request.POST['new_password1']
            pass2 = request.POST['new_password2']
            mail = request.POST['email']
            if pass1 != pass2:
                context['error'] = 1
                return render(request,'registration/password_reset_confirm.html', context)
            user = User.objects.get(email=mail)
            usersql = Userreg.objects.get(email=mail)
            user.set_password(pass1)
            user.save()
            usersql.password = pass1
            usersql.save()
            return render(request,'registration/password_reset_complete.html')
    # validlink = True
    return render(request,'registration/password_reset_confirm.html', context)


