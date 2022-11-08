from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import DrinkPreset, Ingredient, MilkIngredient
from .utils import get_menu, add_item_to_cart, place_order, make_summary
from django.db.models import Q
from account.utils import isEmployee, isManager
import json

def index(request):
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/menu.html', {'item_list': get_menu(), 'employee':employee, 'manager':manager})

def view_item(request, item):
  drink = get_object_or_404(DrinkPreset, name=item)
  milk_list = MilkIngredient.objects.all()
  toppings_list = Ingredient.objects.filter()
  return render(request, 'menu/item.html', {'name':drink.name, 'drink':drink.order, 'milk_list':milk_list, 'toppings_list':toppings_list})

@csrf_exempt
@login_required
def add_to_cart(request):
  if request.method == 'POST':
    item = json.loads(request.body)
    print(item)
    
    if add_item_to_cart(request.user, item):
      return redirect('/menu')
    else:
      return JsonResponse({'Error':True})
  redirect("menu/cart/")

@csrf_exempt
@login_required
def view_cart(request):
  if request.method == 'POST':
    place_order(request.user)
    print('HI!')
    return redirect('/menu/confirm', )
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/cart.html', {'order':make_summary(request.user), 'employee':employee, 'manager':manager}) 


@login_required
def view_confirm(request):
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/confirm.html', {'employee':employee, 'manager':manager})
# Create your views here.