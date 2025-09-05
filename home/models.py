from django.db import models
from django.contrib.auth.models import User

class Prod(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.TextField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=500,default='Other')
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.pname


class Prod_Image(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE, related_name='prod_images')
    image = models.ImageField(upload_to='prod')
    

class ProdBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    destination = models.CharField(max_length=300)
    message = models.TextField()


    def __str__(self):
        return self.fullname +'--'+ self.email
    

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    reference = models.ImageField(upload_to='reference', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.fullname +'--'+ self.email
    