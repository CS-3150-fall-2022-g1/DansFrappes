from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
from .models import DrinkPreset, Ingredient, MilkIngredient
from .utils import get_menu, add_item_to_cart
from django.db.models import Q
import json

def index(request):
  return render(request, 'menu/menu.html', {'item_list': get_menu()})

def view_item(request, item):
  drink = get_object_or_404(DrinkPreset, name=item)
  milk_list = MilkIngredient.objects.all()
  toppings_list = Ingredient.objects.all()
  return render(request, 'menu/item.html', {'name':drink.name, 'drink':drink.order, 'milk_list':milk_list, 'toppings_list':toppings_list})

@csrf_exempt
@login_required
def add_to_cart(request):
  if request.method == 'POST':
    item = json.loads(request.body)
    print(item)
    
    if add_item_to_cart(request.user, item):
      return redirect('/menu')

# Create your views here.