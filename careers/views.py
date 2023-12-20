from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def careers_ins(request):
    template = loader.get_template("careers/careers.html")
    context = {
        "careers_page":"join us",
        }
     
    return HttpResponse(template.render(context, request))