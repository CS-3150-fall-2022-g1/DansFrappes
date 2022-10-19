from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

from account.models import UserAccount


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

@csrf_exempt
def login_screen(request):
  context= {
        'validLogin': True,
        }
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is not None and password is not None:
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect("/menu/")
      else:
        context= {
        'validLogin': False,
        }
  return render(request, "account/login.html", context)

@csrf_exempt
def createaccount(request):
  context= {
        'missingFN': False,
        'missingLN' : False,
        'missingUN': False,
        'missingEM': False,
        'missingpsw': False,
        'matchpsswd': True,
        }
  if request.method == "POST":
    password = request.POST.get('password')
    cpassword = request.POST.get('confirmpassword')
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('firstname')
    last_name = request.POST.get('lastname')
    valid = True
    if password == "":
      valid = False
      context['missingpsw'] = True
    if cpassword != password:
      valid = False
      context['matchpsswd'] = False
    if first_name == "":
      valid = False
      context['missingFN'] = True
    if last_name == "":
      valid = False
      context['missingLN'] = True
    if username == "":
      valid = False
      context['missingUN'] = True
    if email == "":
      valid = False
      context['missingEM'] = True

    # method signature is create_user(username, email, password)
    # using email as username for now
    if valid:
      user = UserAccount.objects.create_user(username, email, password)

      # user is already saved to the database at this point

      user.first_name = first_name
      user.last_name = last_name
      user.save()
      login(request, user)
      return redirect("/menu/")
  return render(request, "account/create.html", context)
# Create your views here.
