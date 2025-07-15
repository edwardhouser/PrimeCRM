from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField()
    addressLineOne = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    stateProv = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    lastcontactdate = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.TextField()
    addressLineOne = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    stateProv = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return (f"{self.firstname} {self.lastname}")
    
    def get_absolute_url(self):
        return reverse("contactdetail", args=[self.id])

