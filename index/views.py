from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


# Create your views here.
    # return HttpResponse("website under construction !!!")
def index_ins(request):
    template = loader.get_template("index/main_index.html")
    context = {
        "index_page":"hello world",
        }
     
    return HttpResponse(template.render(context, request))

     