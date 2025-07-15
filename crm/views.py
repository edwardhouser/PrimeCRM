from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Company, Contact
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class ContactList(ListView):
    template_name = "crm/contactlist.html"
    model = Contact
    
class ContactsNeedUpdate(ListView):
    template_name = "crm/contactupdated.html"
    queryset = Contact.objects.all().order_by('-lastcontactdate')
    model = Contact

class ContactsByCompany(ListView):
    template_name = "crm/contactupdated.html"
    queryset = Contact.objects.all().order_by('company')
    model = Contact


class ContactDetail(DetailView):
    template_name = "crm/contactdetails.html"
    model = Contact


class ContactCreate(CreateView):
    template_name = "crm/contactnew.html"
    model = Contact
    fields = [ 
        "firstname", "lastname", "phone", "email", "company", "birthday", "lastcontactdate", "notes", "addressLineOne", "city", "stateProv", "zipcode"
    ]

class ContactEdit(UpdateView):
    template_name = "crm/contactedit.html"
    model = Contact
    fields = [ 
        "firstname", "lastname", "phone", "email", "company", "birthday", "lastcontactdate", "notes", "addressLineOne", "city", "stateProv", "zipcode"
    ]


class ContactDelete(DeleteView):
    template_name = "crm/contactdelete.html"
    model = Contact
    success_url = reverse_lazy("contact_list")

class CompanyList(ListView):
    template_name = "crm/companylist.html"
    model = Company

class CompanyDetail(DetailView):
    model = Company