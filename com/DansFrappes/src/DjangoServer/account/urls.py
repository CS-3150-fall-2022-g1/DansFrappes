from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('addfunds/', views.funds, name='funds'),
    path('view/', views.view, name='view'),
    path('createaccount/', views.createaccount, name='create'),
    path('login/', views.login_screen, name='login'),
    path('addhours/', views.add_hours, name='addhours'),
    path('alluseraccounts/', views.see_all_users, name='allusers'),
    path('logout/', views.user_logout, name='logout')
]