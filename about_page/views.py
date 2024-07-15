from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.http import Http404


from django.views.generic import ListView, DetailView


from .models import About_page

class AboutPageListView(ListView):
    model = About_page
    template_name = "about_page.html"

class AboutPageDetailView(DetailView):
    model = About_page
    template_name = "about_page.html"





# Create your views here.
    # return HttpResponse("website under construction !!!")
def about_func(request):
   # if request.LANGUAGE_CODE == 'de-at':
        #return HttpResponse("You prefer to read Austrian German.")
    #else:
        #return HttpResponse("You prefer to read another Language.")
     

    template = loader.get_template("about/about_page.html")
    context = {
        "about":"about_us",
        }
     
    #return render(request, "about/about_page.html", context)
    return HttpResponse(template.render(context, request))


