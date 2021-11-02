from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('changepassword/',views.changepassword, name='changepassword'),
    path('password_reset/',views.password_reset, name='password_reset'),

  


]
