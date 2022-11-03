from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('queue/', views.queue, name='queue'),
    path('payemployees/', views.payemployees, name='pay'),
    path('payemployee/', views.payemployee, name='pay'),
    path('fulfillorder/', views.fulfillOrder, name='pay'),
    path('editemployee/', views.editWage, name='edit'),
    path('', views.employee, name='employee'),


]