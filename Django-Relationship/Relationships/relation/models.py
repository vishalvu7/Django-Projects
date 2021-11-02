from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=10)
    acc_holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bankname")


    def __str__(self):
        return self.name


class Phone(models.Model):
    phone = models.CharField(max_length=10)
    phone_id = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.phone


class Song(models.Model):
   
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])






