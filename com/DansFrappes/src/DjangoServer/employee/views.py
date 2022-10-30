from django.http import HttpResponse
from django.shortcuts import render, redirect



def inventory(request):
    page_title = 'Inventory'
    return render(request, 'employee/inventory.html', {'page_title': page_title})

def queue(request):
    page_title = 'Order Queue'
    return render(request, 'employee/queue.html', {'page_title': page_title})

def employee(request):
    page_title = 'Employees'
    return render(request, 'employee/employee.html', {'page_title': page_title})