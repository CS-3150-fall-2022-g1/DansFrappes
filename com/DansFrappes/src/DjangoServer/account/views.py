from decimal import Decimal
from turtle import update
from unicodedata import decimal
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

from account.models import UserAccount
from account.utils import create_account, update_account_data, add_funds, isEmployee, isManager

def index(request):
    return redirect('/account/view',permanent=True)

@csrf_exempt
@login_required
def view(request):
    firstname = request.user.first_name
    lastname =  request.user.last_name
    email = request.user.email
    birthday = request.user.birthday
    if birthday != None:
      birthday = birthday.strftime('%Y-%m-%d')
    funds = request.user.funds
    employee = isEmployee(request.user) and not request.user.store
    hoursWorked = request.user.hours_worked
    hourlywage = request.user.hourly_wage
    manager = isManager(request.user)
    return render(request, "account/view.html", 
      {
        'firstname':firstname, 
        'lastname':lastname, 
        'email':email, 
        'birthday': birthday, 
        'funds':funds, 
        'employee':employee,
        'hourlywage':hourlywage,
        'hoursworked':hoursWorked,
        'manager':manager
        })

@csrf_exempt
@login_required
def funds(request):
  if request.method == 'POST':
    amount =  Decimal(float(request.POST.get('amount')))
    print(amount)
    add_funds(request.user, amount)
    return redirect("/account/view/")
  return view(request)

@csrf_exempt
@login_required
def edit(request):
    if request.method == 'POST':
      update_account_data(request.user, request.POST.get('email'), request.POST.get('firstname'), request.POST.get('lastname'), request.POST.get('birthday'))
      return redirect("/account/view/")

    return view(request)

@csrf_exempt
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
      user = create_account(username, email, first_name, last_name, password) # Helper method to create a user with the new UserAccount model

      user.save()
      login(request, user)
      return redirect("/menu/")
  return render(request, "account/create.html", context)
# Create your views here.

@csrf_exempt
def add_hours(request):
  if request.method == 'POST':
      user = request.user
      hours = Decimal(float((request.POST.get('hour'))))
      user.hours_worked = user.hours_worked + hours
      print("Adding hours: "  + str(hours) + " "  +str(user.hours_worked))
      user.save()
      return redirect("/account/view/")

  return view(request)

@login_required
@csrf_exempt
def see_all_users(request):
  if not isManager(request.user):
    return redirect("/menu/")
  
  userList = UserAccount.objects.values()
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, "account/alluseraccounts.html",  {'employee':employee, 'manager':manager, 'all_users':userList})

@login_required
@csrf_exempt
def hireUser(request):
  if not isManager(request.user):
    return redirect("/menu/")
  if request.method == 'POST':
    userid = int(request.POST.get("user_idx"))
    u = UserAccount.objects.get(pk=userid)
    u.setEmployee()
    u.save()
  return redirect("/account/alluseraccounts/")

@login_required
@csrf_exempt
def fireUser(request):
  if not isManager(request.user):
    return redirect("/menu/")
  if request.method == 'POST':
    userid = int(request.POST.get("user_idx"))
    u = UserAccount.objects.get(pk=userid)
    u.setCustomer()
    u.save()
  return redirect("/account/alluseraccounts/")

@login_required
@csrf_exempt
def promoteUser(request):
  if not isManager(request.user):
    return redirect("/menu/")
  if request.method == 'POST':
    userid = int(request.POST.get("user_idx"))
    u = UserAccount.objects.get(pk=userid)
    u.setManager()
    u.save()
  return redirect("/account/alluseraccounts/")

@login_required
@csrf_exempt
def demoteUser(request):
  if not isManager(request.user):
    return redirect("/menu/")
  if request.method == 'POST':
    userid = int(request.POST.get("user_idx"))
    u = UserAccount.objects.get(pk=userid)
    u.setEmployee()
    u.save()
  return redirect("/account/alluseraccounts/")


