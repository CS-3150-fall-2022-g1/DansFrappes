from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.



@login_required
def displayInfo(request):
    return render(request, "login/info.html", {'first': request.user.first_name, 'last': request.user.last_name})

def login_screen(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/login/")
    return render(request, "login/login.html")

def user_logout(request):
    logout(request)
    return redirect("/login/login")

def newUser(request):
    if request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']

        # method signature is create_user(username, email, password)
        # using email as username for now
        user = User.objects.create_user(email, email, password)

        # user is already saved to the database at this point

        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return redirect("/login/")
    return render(request, "login/newuser.html")
