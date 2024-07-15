from django.db import models

from django.urls import reverse


class About_page(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("About_page", args=[str(self.id)])