from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.utils import isEmployee, isManager



def inventory(request):
    page_title = 'Inventory'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    return render(request, 'employee/inventory.html', {'page_title': page_title, 'employee':employee, 'manager':manager})

def queue(request):
    page_title = 'Order Queue'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    return render(request, 'employee/queue.html', {'page_title': page_title, 'employee':employee, 'manager':manager})

def employee(request):
    page_title = 'Employees'
    employee = isEmployee(request.user)
    manager = isManager(request.user)
    return render(request, 'employee/employee.html', {'page_title': page_title, 'employee':employee, 'manager':manager})