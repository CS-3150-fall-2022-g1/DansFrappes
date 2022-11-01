from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<item>', views.view_item, name='menu_item')
]