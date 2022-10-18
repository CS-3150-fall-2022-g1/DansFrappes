from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def index(request):
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
  return render(request, "login/login.html", context)

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
      user = User.objects.create_user(username, email, password)

      # user is already saved to the database at this point

      user.first_name = first_name
      user.last_name = last_name
      user.save()
      login(request, user)
      return redirect("/menu/")
  return render(request, "login/create.html", context)
# Create your views here.

