from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit', views.edit, name='edit'),
    path('view', views.view, name='view'),
    path('create', views.new_user, name='create'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
]