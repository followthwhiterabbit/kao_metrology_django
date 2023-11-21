from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def contact_func(request):
    template = loader.get_template("contact_page/contact_page.html")
    context = {
        "contact":"contact_us",
        }
     
    return HttpResponse(template.render(context, request))