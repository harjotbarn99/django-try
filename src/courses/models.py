from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    avalible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("courses:particularCourse",kwargs={"id" : self.id})