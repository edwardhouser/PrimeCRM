from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("companydetail", args=[self.id])

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return (f"{self.firstname} {self.lastname}")
    
    def get_absolute_url(self):
        return reverse("contactdetail", args=[self.id])

class Deal(models.Model):
    status_choices = [
        ('opportunity', '1-Opportunity'),
        ('qualification', '2-Qualification'),
        ('negotiation', '3-Negotiation'),
        ('closed', 'Closed (Won)'),
        ('Lost', 'Closed (Lost)'),

    ]
    title = models.CharField(max_length=200)
    expectedclosedate = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    notes = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default='opportunity')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("dealdetail", args=[self.id])
