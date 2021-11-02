from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def email(request):    
    if request.method == 'POST':
        recep_email = request.POST.get('email')
        name = request.POST.get('name')

        if recep_email:


            subject = name + "," + 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [recep_email,]   
            send_mail( subject, message, email_from, recipient_list ) 
            messages.success(request, 'Email Sent Successfully...')  
            return redirect('index')
        else:
            messages.error(request,"Error Occurred")
            return render( request,"index.html" )

    return render(request, 'index.html')

 