from django.shortcuts import redirect, render
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def sign_up(request):
    context = {}
    context['error']=''
    if request.method == "POST":
        fname = request.POST.get('first_name')  
        lname = request.POST.get('last_name')
        uname = request.POST.get('user_name_1')
        password_a1 = request.POST.get('password_1')
        password_a2 = request.POST.get('password_2')
        if password_a1 != password_a2:
            context['error'] = "Second password is Wrong"
            return render(request,'register/sign_up.html',context) 
        if  fname == "" or lname == "" or uname == "" or password_a1 == "" or password_a2 == "":
            context['error'] = "Check your information, plaase" 
            return render(request,'register/sign_up.html',context) 

        user_check = User.objects.filter(username = uname)

        if len(user_check) != 0:
            context['error'] = "This user has"
            return render(request,'register/sign_up.html',context)  

        user = User.objects.create_user(first_name=fname,last_name=lname,username = uname,password = password_a1)
        user.save()
       
        if user is not None:
            return redirect('in')
    
    return render(request,'register/sign_up.html',context)

def sign_in(request):
    context = {}
    if request.method == 'POST':
        
        username = request.POST.get('user_name_2')
        password = request.POST.get('password_3')
        if username == "" or password == "":
            context['error'] = 'Check your information'
            return render(request,'register/sign_in.html',context)
        user = authenticate(request,username = username, password = password)
       
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['error'] = 'Password or User is not has'
    return render(request,'register/sign_in.html', context)

@login_required
def logout_view(request):
    if request.method=='GET':
        logout(request)
        return redirect('in')


