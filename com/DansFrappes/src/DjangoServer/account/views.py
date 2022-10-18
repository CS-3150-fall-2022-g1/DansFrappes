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

@login_required
def edit(request):
    if request.method == 'POST':
        return

    return HttpResponse("Edit Account")

def user_logout(request):
    logout(request)
    return redirect("/account/login")