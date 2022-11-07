from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.utils import isEmployee, isManager
from account.models import UserAccount
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt

from menu.models import Order, Ingredient



def inventory(request):
    page_title = 'Inventory'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    ingredients = Ingredient.objects.values()
    return render(request, 'employee/inventory.html', {'page_title': page_title, 'employee':employee, 'manager':manager, 'ingredients':ingredients})

def queue(request):
    page_title = 'Order Queue'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    orders = Order.objects.values()
    return render(request, 'employee/queue.html', {'page_title': page_title, 'employee':employee, 'manager':manager, 'orders':orders})

def employee(request):
    page_title = 'Employees'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    group = Group.objects.get(name="employee")
    empList = group.user_set.all()
    return render(request, 'employee/employee.html', {'page_title': page_title, 'employee':employee, 'manager':manager, 'empList':empList})

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

@csrf_exempt
def payemployee(request):
    if not isManager(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        empId = int(request.POST.get("user_idx"))
        u = UserAccount.objects.get(pk=empId)
        u.pay()
    return redirect("/employee/")

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

def fulfillOrder(request):
    if not isEmployee(request.user):
        return redirect("/menu/")
    if request.method == 'POST':
        orderid = int(request.POST.get("order_idx"))
        order = Order.objects.get(pk=orderid)
        order.fulfilled = True
        order.save()
    return redirect("/employee/queue/")