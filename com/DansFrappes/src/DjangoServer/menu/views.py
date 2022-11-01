from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import DrinkPreset

def index(request):
  return render('menu/menu.html')

# def view_item(request, item):
#   drink = DrinkPreset.objects.get(name=item)
#   return render(request, 'menu/item.html', {})

# Create your views here.