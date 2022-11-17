from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.utils import isEmployee, isManager
from account.models import UserAccount
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from menu.models import Order, Ingredient, MilkIngredient
from decimal import Decimal
import json


@login_required
def inventory(request):
    page_title = 'Inventory'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    ingredients = Ingredient.objects.values()
    milkIngredients = MilkIngredient.objects.values()
    names = '^'.join([i['name'] for i in Ingredient.objects.values()])
    milkNames = '^'.join([i['name'] for i in MilkIngredient.objects.values()])
    names += '^' + milkNames
    print(names)
    prices = json.dumps({i["name"]: str(i["buy_cost"]) 
        for i in list(Ingredient.objects.values()) + list(MilkIngredient.objects.values())})
    balance = UserAccount.objects.filter(store=True)[0].funds

    return render(request, 'employee/inventory.html', 
    {'page_title': page_title, 
    'employee':employee, 
    'manager':manager, 
    'ingredients':ingredients,
    'milkIngredients':milkIngredients, 
    'names':names,
    'milkNames':milkNames, 
    'prices':prices,
    'balance':balance})

@login_required
def queue(request):
    page_title = 'Order Queue'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    orders = Order.objects.values()
    users = UserAccount.objects.values()
    return render(request, 'employee/queue.html', {'page_title': page_title, 'employee':employee, 'manager':manager, 'orders':orders, 'users': users})

@login_required
def employee(request):
    page_title = 'Employees'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    group = Group.objects.get(name="employee")
    empList = group.user_set.exclude(store=True).all()
    return render(request, 'employee/employee.html', {'page_title': page_title, 'employee':employee, 'manager':manager, 'empList':empList})

@login_required
@csrf_exempt
def payemployees(request):
    if not isManager(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        group = Group.objects.get(name="employee")
        empList = group.user_set.all()
        for e in empList:
            e.pay()
    return redirect("/employee/")

@login_required
@csrf_exempt
def payemployee(request):
    if not isManager(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        empId = int(request.POST.get("user_idx"))
        u = UserAccount.objects.get(pk=empId)
        u.pay()
    return redirect("/employee/")

@login_required
@csrf_exempt
def editWage(request):
    if not isManager(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        empId = int(request.POST.get("user_idx"))
        u = UserAccount.objects.get(pk=empId)
        wage = float(request.POST.get('hourlywage'))
        u.setWage(wage)
        u.save()
    return redirect("/employee/")

@login_required
@csrf_exempt
def fulfillOrder(request):
    if not isEmployee(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        orderid = int(request.POST.get("order_idx"))
        order = Order.objects.get(pk=orderid)
        order.fulfilled = True
        order.save()
    return redirect("/employee/queue/")

@login_required
@csrf_exempt
def buy(request):
    # if not isEmployee(request.user):
    #     return redirect("/menu/")
    if request.method == 'POST':
        counts, bill = json.loads(request.body).items()
        for name,count in counts[1].items():
            # print(name,count)
            e = Ingredient.objects.filter(name=name)
            if(len(e) > 0):
                e = e[0]
            else:   
                e = MilkIngredient.objects.filter(name = name)[0]
            e.stock += count
            e.save()
        manager = UserAccount.objects.filter(manager=True)[0]
        manager.funds -= Decimal(bill[1])
        manager.save()
    return redirect("/employee/inventory")