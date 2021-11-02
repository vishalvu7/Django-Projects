
from . import views
from django.urls import path

urlpatterns = [
   path('onetoone/',views.onetoone,name='onetoone'),
   path('onetoomany/',views.onetomany,name='onetoomany'),
   path('manytoomany/',views.manytoomany,name='manytoomany')

]
