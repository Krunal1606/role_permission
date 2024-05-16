from django.shortcuts import render
from accounts.forms import UserCreateForm
from django.shortcuts import redirect
from  django.contrib.auth.forms import AuthenticationForm
from  .models  import CustomUser
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#  import http
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.

# create user signup
def userSignUp(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'userSignup.html',{'form':form})
    else:
        form = UserCreateForm()
        return render(request,'userSignup.html',{'form':form})

def userLogin(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            roll = CustomUser.objects.get(username=user).role
            apr = CustomUser.objects.get(username=user).approval
            if user is not None and apr:
                if roll == 'subscriber' and apr:
                    login(request,user)
                    return  HttpResponse("Subscriber")
                elif roll == 'student' and apr:
                    login(request,user)
                    return  HttpResponse("Student")
                elif roll == 'teacher' and apr:
                    login(request,user)
                    return  HttpResponse("Teacher")
                elif roll == 'editor' and apr:
                    login(request,user)
                    return  HttpResponse("Editor")
                elif roll == 'admin' and apr:
                    login(request,user)
                    return  HttpResponse("Admin")
                else:
                    return render(request,'userLogin.html',{'form':form})
            else:
                messages.error(request, "User not approved")
                return render(request,'userLogin.html',{'form':form})
        else:
            return render(request,'userLogin.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request,'userLogin.html',{'form':form})
