from django.conf import settings
from django.shortcuts import render , redirect
from . models import Contact
from accounts.models import Account
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='accounts:login')
def contact(request):
    if request.method == 'POST':
        account = Account.objects.get(user = request.user)
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        Contact.objects.create(
            account=account,
            subject=subject,
            email=email,
            message=message,
        )
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently = False,
        )
        return redirect('home')

    return render(request , 'contact/contact.html')