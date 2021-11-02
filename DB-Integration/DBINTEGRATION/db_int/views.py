from django.shortcuts import render
from django.contrib import messages

from db_int.models import Student

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        psw1 = request.POST.get('psw')
        psw2 = request.POST.get('psw-repeat')

        if psw1 == psw2:
            student = Student(email=email,password=psw1)
            student.save()
            messages.success(request, 'Profile details updated.')
            return render(request, 'index.html')
        else:
            messages.error(request, 'index.html')
            return render(request, 'index.html')
    return render(request, 'index.html')