from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from store.forms import CustomUserForm

# Registration Page
def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfully ! Login to continue")
            return  redirect('/login')
        context = {"form":form}
    return render(request,'store/auth/register.html')
    #return render(request,'store/auth/register.html')

#Login Page
def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')
    else:
        if request.method =="POST":
            name=request.POST.get('Username')
            psswd=request.POST.get("Password")
            user = authenticate(request,username = name, password = psswd)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid username and password")
                return redirect('/login')
    return render(request,"store/auth/login.html")

#Logout Page
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect('/')