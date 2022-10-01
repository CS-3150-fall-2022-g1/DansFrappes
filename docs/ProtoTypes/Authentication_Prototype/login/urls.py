from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.displayInfo, name='index'),
    path('info', views.displayInfo, name='info'),
    path('login', views.login_screen, name='login'),
    path('account/create', views.newUser, name='create'),
    path('account/logout', views.user_logout, name="logout")
]