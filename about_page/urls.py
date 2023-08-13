from django.urls import path 

from . import views

urlpatterns = [
    path("", views.about_func, name="about_page"),
]

