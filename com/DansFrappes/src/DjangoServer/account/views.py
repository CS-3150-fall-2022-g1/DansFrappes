import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .utils import createAccount

def index(request):
    return redirect('/account/view',permanent=True)

@login_required
def view(request):
    name = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    birthday = request.user.birthday
    funds = request.user.funds

    return render(request, "account/view.html", {'name':name, 'email':email, 'birthday': birthday, 'funds':funds})

def edit(request):
    if request.method == 'POST':
        return

    return HttpResponse("Edit Account")

def new_user(request):
    if request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']

        # method signature is create_user(username, email, password)
        # using email as username for now
        user = createAccount(email, first_name, last_name, password)
        user.save()

        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)

        return redirect("/account/view")
    
    return render(request, "account/create.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/menu/")
    return render(request, "account/login.html")

def user_logout(request):
    logout(request)
    return redirect("/account/login")