from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('allmembers/',views.show,name='allmembers'),
    path('allmembers/edit/<int:id>',views.edit,name='allmembers'),
    path('allmembers/delete/<int:id>',views.deletemember,name='delete')




]