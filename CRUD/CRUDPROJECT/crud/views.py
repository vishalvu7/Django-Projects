from crud.models import Member
from django.shortcuts import redirect, render

# Create your views here.

def index(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        password = request.POST.get('psw')

        member = Member(name=name, email=email, city=city, password=password)
        member.save()


    return render(request, 'index.html')


def show(request):
    if request.method == 'GET':
        allmembers = Member.objects.all()
        return render(request, 'allmembers.html',{'members':allmembers})


def edit(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        password = request.POST.get('psw')
        m = Member.objects.get(id=id)
        m.name = name
        m.email = email
        m.city = city
        m.password = password
        m.save()
        return redirect('allmembers')
    else:

        member = Member.objects.get(id=id)
        return render(request, 'edit.html',{'member':member})
       
    


def deletemember(request,id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect('allmembers')