from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def newsnevents_func(request):
    template = loader.get_template("newsnevents/newsnevents.html")
    context = {
        "news_n_events":"our_events_n_news",
        }
     
    return HttpResponse(template.render(context, request))