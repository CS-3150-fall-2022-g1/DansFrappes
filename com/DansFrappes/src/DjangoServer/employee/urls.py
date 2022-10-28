from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('queue/', views.queue, name='queue'),
    path('staff/', views.staff, name='staff'),


]