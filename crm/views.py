from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Company, Contact, Deal
from django.urls import reverse_lazy
from django import forms

# Create your views here.

# Contact Views 

class ContactList(ListView):
    template_name = "crm/contactlist.html"
    model = Contact

    def get_queryset(self):
        logged_user = self.request.user
        return Contact.objects.filter(author = logged_user)
    
class ContactsNeedUpdate(ListView):
    template_name = "crm/contactupdated.html"
        
    def get_queryset(self):
        logged_user = self.request.user
        return Contact.objects.filter(author = logged_user).order_by('-lastcontactdate')
    model = Contact

class ContactsByCompany(ListView):
    template_name = "crm/contactupdated.html" 
    model = Contact

    def get_queryset(self):
        logged_user = self.request.user
        return Contact.objects.filter(author = logged_user).order_by('company')


class ContactDetail(DetailView):
    template_name = "crm/contactdetails.html"
    model = Contact

    def get_queryset(self):
        logged_user = self.request.user
        return Contact.objects.filter(author = logged_user)


class ContactCreate(CreateView):
    template_name = "crm/contactnew.html"
    model = Contact
    fields = [ 
        "firstname", "lastname", "phone", "email", "company", "birthday", "lastcontactdate", "notes", "addressLineOne", "city", "stateProv", "zipcode"
    ]
    def form_valid(self, form):
        # before saving the record
        # set the author to be the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

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


#Company Views


class CompanyList(ListView):
    template_name = "crm/companylist.html"
    model = Company

    def get_queryset(self):
        logged_user = self.request.user
        return Company.objects.filter(author = logged_user)

class CompanyDetail(DetailView):
    template_name = "crm/companydetails.html"
    model = Company

class CompanyByIndustry(ListView):
    template_name = "crm/companyindustry.html"
    model = Company
    
    def get_queryset(self):
        logged_user = self.request.user
        return Company.objects.filter(author = logged_user).order_by('industry')
  

class CompanyCreate(CreateView):
    template_name = "crm/companynew.html"
    model = Company
    fields = [ 
        "name", "industry", "phone", "notes", "addressLineOne", "city", "stateProv", "zipcode"
    ]

    def form_valid(self, form):
        # before saving the record
        # set the author to be the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class CompanyEdit(UpdateView):
    template_name = "crm/companyedit.html"
    model = Company
    fields = [ 
        "name", "industry", "phone", "notes", "addressLineOne", "city", "stateProv", "zipcode"
    ]

class CompanyDelete(DeleteView):
    template_name = "crm/companydelete.html"
    model = Company
    success_url = reverse_lazy("company_list")



# Deal Views


class DealList(ListView):
    template_name = "crm/deallist.html"
    model = Deal

    def get_queryset(self):
        logged_user = self.request.user
        return Deal.objects.filter(author = logged_user)

class DealDetails(DetailView):
    template_name = "crm/dealdetails.html"
    model = Deal

class DealCreate(CreateView):
    template_name = "crm/dealnew.html"
    model = Deal
    fields = [
        "title", "expectedclosedate", "amount", "company", "notes", "status"
    ]

    def form_valid(self, form):
        # before saving the record
        # set the author to be the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class DealEdit(UpdateView):
    template_name = "crm/dealedit.html"
    model = Deal
    fields = [
        "title", "expectedclosedate", "amount", "company", "notes", "status"
    ]

class DealDelete(DeleteView):
    template_name = "crm/dealdelete.html"
    model = Deal

class DealbyStatus(ListView):
    template_name = "crm/dealbystatus.html"
    model = Deal
    def get_queryset(self):
        logged_user = self.request.user
        return Deal.objects.filter(author = logged_user).order_by('status')


class DealbyCloseDate(ListView):
    template_name = "crm/dealbyclosedate.html"
    model = Deal
    
    def get_queryset(self):
        logged_user = self.request.user
        return Deal.objects.filter(author = logged_user).order_by('-expectedclosedate')
   