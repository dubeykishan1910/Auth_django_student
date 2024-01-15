from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from hr_app.models import Hr

# Create your views here.
def register_candidate(request):
    if request.method == 'POST':
        # Geting data from forms 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/candidate_register.html',{'msg':msg})
        
        if User.objects.filter(username=username).exists():
            msg = 'User already Exists...'
            return render(request,'authuser/candidate_register.html',{'msg':msg})

        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
        return redirect ('candidate_dashbordh')
    
    return render(request,'authuser/candidate_register.html')




def register_hr(request):
    if request.method == 'POST':
        # Geting data from forms 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/candidate_register.html',{'msg':msg})
        
        if User.objects.filter(username=username).exists():
            msg = 'User already Exists...'
            return render(request,'authuser/candidate_register.html',{'msg':msg})

        user = User.objects.create_user(username=username,email=email,password=password)
        Hr(user=user).save()
        
        login(request,user)
        return redirect ('candidate_dashbordh')

    return render(request,'authuser/hr_register.html')



