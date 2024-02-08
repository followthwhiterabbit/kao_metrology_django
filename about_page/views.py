from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404



# Create your views here.
    # return HttpResponse("website under construction !!!")
def about_func(request):
    template = loader.get_template("about/about_page.html")
    context = {
        "about":"about_us",
        }
     
    return HttpResponse(template.render(context, request))


