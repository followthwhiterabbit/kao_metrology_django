from django.urls import path 

from . import views

urlpatterns = [
    path("", views.newsnevents_func, name="newsnevents_page"),
]

