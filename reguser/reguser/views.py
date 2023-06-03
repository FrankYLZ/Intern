from django.shortcuts import render
from reguser.models import Userreg
from django.contrib import messages

def Userregistration(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('password') and request.POST.get('gender'): 
            saverecord = Userreg()
            saverecord.username = request.POST.get('username')
            saverecord.email = request.POST.get('email')
            saverecord.password = request.POST.get('password')
            saverecord.gender = request.POST.get('gender')
            saverecord.save()
            messages.success(request, "New User Registration Details Saved Successfully..!")
            return render(request,'Index.html')
    else:
        return render(request,'Index.html')
