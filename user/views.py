from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm

# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)
            newUser.save()

            login(request,newUser)
            messages.success(request, "Başarıyla Giriş Yaptınız.")
            return redirect("index")
    else:
        form = RegisterForm()
        context = {
        "form": form,
        }
        return render(request,"register.html",context=context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

def loginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
         username = form.cleaned_data.get("username")
         password = form.cleaned_data.get("password")

         user = authenticate(username = username,password = password)

         if user is None:
             messages.info(request,"Kullanıcı Adı yada parola Hatalı")
         else:
            messages.success(request,"Başarıyla Giriş yaptınız")
            login(request,user)
            return redirect("index")
    context = {
    "form" : form
    }
    return render(request,"login.html",context)