from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create user
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,password=password)
        user.save()

        return render(request, 'index.html')

    else:
       return render(request, 'index.html')



def loginuser(request):
    # return render(request, 'login.html')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            usr = User.objects.get(username=user.username)
            request.session['user_id'] = usr.id
            login(request, user)
            return redirect('profile')
                
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required(login_url='/login/')
# @login_required(login_url='/accounts/login/')
def profile(request):

    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        return render(request, 'profile.html',{'users':user})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def logout_user(request):

    del request.session['user_id']
    return redirect('login')

def password_reset(request):


    if request.method == 'POST':

        email = request.POST.get('email')


        try:

            u = User.objects.get(email=email)
            try:
                if u is not None:

                    request.session['uid'] = u.id
                   
                   

                    
                    
                    subject = 'Password Reset'
                    message = ' Your OTP for resetting password is - '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email,]    
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('changepassword')


            except Exception:
                messages.error(request, 'Invalid email')
                return render(request, 'password_reset')

                
        except:
            messages.error(request,'Invalid')
            return render(request, 'password_reset.html')
        
        return render(request, 'password_reset.html')
    
      
           

    return render(request, 'password_reset.html')


def changepassword(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('repeatpassword')
       
        uid = request.session['uid']
        usrs = User.objects.get(id=uid)

        if password1 == password2 :

            usrs.set_password(password1)
            usrs.save()

           
            

           
            del request.session['uid']
            return redirect('/login/')

        else:
            messages.error(request, 'Invalid otp or password')
            return render(request, 'changepassword.html')


       

    return render(request, 'changepassword.html')
   
