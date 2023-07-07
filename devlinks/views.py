from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings



def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form', # titulo
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )

    return render(request, 'index.html')
    # template_name = "links.html"
