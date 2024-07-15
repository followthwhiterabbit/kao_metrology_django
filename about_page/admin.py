from django.contrib import admin

# Register your models here.

from .models import About_page

class URLAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

admin.site.register(About_page, URLAdmin) 

