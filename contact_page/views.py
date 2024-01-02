from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404

from django.core.mail import send_mail
from django.conf import settings
import re


def validate_email_address(email_address):

   return re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address)

def contact_func(request, ):
    template = loader.get_template("contact_page/contact_page.html")
    context = {
        "contact":"contact_us",
        }

    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']

        if not validate_email_address(email):
            return HttpResponse("Invalid email address")


        send_mail(
            name, #title
            message + '\nsend by ' + email,
            request.POST['email'],
            ['karaaliogluseyit@gmail.com'], #receiver email
            fail_silently=False, 
        )

    return HttpResponse(template.render(context, request))


    

