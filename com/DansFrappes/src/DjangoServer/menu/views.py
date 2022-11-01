from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import DrinkPreset
from .utils import get_menu

def index(request):
  return render(request, 'menu/menu.html', {'item_list': get_menu()})

def view_item(request, item):
  # drink = DrinkPreset.objects.get(name=item)
  return render(request, 'menu/item.html', {})

# Create your views here.