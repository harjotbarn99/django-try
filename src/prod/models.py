from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank= True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField(default="cool dd")
    featured = models.BooleanField(default=True )

    def getUrl(self):
        return reverse("prod:particularProd",kwargs={"id" : self.id})
        # return f'/dynamic/{self.id}/'
