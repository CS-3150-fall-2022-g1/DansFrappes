from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('queue/', views.queue, name='queue'),
    path('employee/', views.employee, name='employee'),


]