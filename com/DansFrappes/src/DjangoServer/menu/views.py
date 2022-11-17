from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
  toppings_list = Ingredient.objects.all()
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/item.html', {'name':drink.name, 'drink':drink.order, 'milk_list':milk_list, 'toppings_list':toppings_list, 'employee':employee, 'manager':manager})

@csrf_exempt
@login_required
def add_to_cart(request):
  if request.method == 'POST':
    item = {}
    for key, value in request.POST.items():
      if key == 'milk' or key == 'name':
        item[key] = value
      else:
        try:
          num = int(value)
          if num > 0:
            item[key] = num
        except:
          pass
    if add_item_to_cart(request.user, item):
      return redirect('/menu')
  return redirect("/menu")

@login_required
def remove_from_cart(request, index):
  if len(request.user.cart.get('items')) > 0 and len(request.user.cart.get('items')) > index:
    del request.user.cart.get('items')[index]
    request.user.save()
  return redirect(reverse('cart'))

@csrf_exempt
@login_required
def view_cart(request):
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  if request.method == 'POST':
    confirm = place_order(request.user)
    return render(request, 'menu/confirm.html', {'employee':employee, 'manager':manager, 'confirmed': confirm})
  return render(request, 'menu/cart.html', {'order':make_summary(request.user), 'employee':employee, 'manager':manager}) 

@login_required
def view_confirm(request):
  employee = isEmployee(request.user)
  manager = isManager(request.user)
  return render(request, 'menu/confirm.html', {'employee':employee, 'manager':manager})
# Create your views here.