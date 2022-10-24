from django.http import HttpResponse
from django.shortcuts import render, redirect



def inventory(request):
    return render(request, 'employee/inventory.html')