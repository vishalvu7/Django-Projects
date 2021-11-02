from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from relation.models import Bank, Phone, Song
from django.db import models
import django.apps



# Create your views here.

#OneToOne Relationship
def onetoone(request):
    # single = User.objects.get(id=2).phone
    ph = Phone.objects.get(phone='8658745921').id

    return HttpResponse("<h2>{}</h2>".format(ph))

# OneToMany Relationship
def onetomany(request):
    
    # user = User.objects.get(username='vishal@1234+')
    # bank = Bank.objects.all().filter(acc_holder=user)  
    # print(bank)
    us = Bank.objects.get(id=2)
    users = User.objects.get(id=us.id)
    print(users)


    return HttpResponse("hello")


def manytoomany(request):



    # user = User.objects.get(username='sakshi@1234+')
    # print(Song.objects.filter(user=user))

    # song = Song.objects.get(name='Tere Bina')
    # print(song.User.username)


    # song = Song.objects.get(name='Tere Bina').user.all()
    song = Song.objects.get(id=11).user.all()

    print(song)

   
    
    return HttpResponse("Hello")

