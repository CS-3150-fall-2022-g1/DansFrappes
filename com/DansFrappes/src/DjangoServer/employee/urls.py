from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('queue/', views.queue, name='queue'),
    path('payemployees/', views.payemployees, name='paymany'),
    path('payemployee/', views.payemployee, name='payone'),
    path('fulfillorder/', views.fulfillOrder, name='fulfil'),
    path('editemployee/', views.editWage, name='edit'),
    path('', views.employee, name='employee'),
    path('buy/', views.buy, name='buy')


]