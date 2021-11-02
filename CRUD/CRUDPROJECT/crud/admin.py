from crud.models import Member
from django.contrib import admin

# Register your models here.

class Memberadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'city','password']
admin.site.register(Member,Memberadmin)