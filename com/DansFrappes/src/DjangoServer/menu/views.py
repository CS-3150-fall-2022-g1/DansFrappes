from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import DrinkPreset, Ingredient, MilkIngredient
from .utils import get_menu
from django.db.models import Q
from account.utils import isEmployee, isManager

def index(request):
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/menu.html', {'item_list': get_menu(), 'employee':employee, 'manager':manager})

def view_item(request, item):
  drink = DrinkPreset.objects.get(name=item)
  milk_list = MilkIngredient.objects.all()
  toppings_list = Ingredient.objects.all()
  return render(request, 'menu/item.html', {'name':drink.name, 'drink':drink.order, 'milk_list':milk_list, 'toppings_list':toppings_list})

# Create your views here.