from django.http import HttpResponse
from django.shortcuts import render, redirect



def inventory(request):
    return render(request, 'employee/inventory.html')

def queue(request):
    return render(request, 'employee/queue.html')

def staff(request):
    return render(request, 'employee/staff.html')