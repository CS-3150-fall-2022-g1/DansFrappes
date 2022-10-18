from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

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
        return redirect("/createaccount/")
      else:
        context= {
        'validLogin': False,
        }
  return render(request, "login/login.html", context)

def createaccount(request):
  template = loader.get_template('login/create.html')
  return HttpResponse(template.render())
# Create your views here.

