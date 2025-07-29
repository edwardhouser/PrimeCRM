from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactList.as_view(), name="contact_list"),
    path("contacts/", views.ContactList.as_view(), name = "contact_list"),
    path("contacts/lastcontacted", views.ContactsNeedUpdate.as_view(), name = "contact_lastcontacted"),
    path("contacts/contactbycompany", views.ContactsByCompany.as_view(), name = "contact_bycompany"),
    path("contacts/<int:pk>/", views.ContactDetail.as_view(), name = "contactdetail"),
    path("contacts/<int:pk>/edit", views.ContactEdit.as_view(), name = "contactedit"),
    path("contacts/<int:pk>/delete", views.ContactDelete.as_view(), name = "contact_delete"),
    path("contacts/new", views.ContactCreate.as_view(), name = "contact_new"),

    path("company/", views.CompanyList.as_view(), name = "company_list"),
    path("company/industry", views.CompanyByIndustry.as_view(), name = "company_byindustry"),
    path("company/<int:pk>/", views.CompanyDetail.as_view(), name = "companydetail"),
    path("company/<int:pk>/edit", views.CompanyEdit.as_view(), name = "companyedit"),
    path("company/<int:pk>/delete", views.CompanyDelete.as_view(), name = "company_delete"),
    path("company/new", views.CompanyCreate.as_view(), name = "company_new"),

    path("deals/", views.DealList.as_view(), name = "deal_list"),
    path("deals/<int:pk>/", views.DealDetails.as_view(), name = "dealdetail"),
    path("deals/<int:pk>/edit", views.DealEdit.as_view(), name = "dealedit"),
    path("deals/<int:pk>/delete", views.DealDelete.as_view(), name = "deal_delete"),
    path("deals/new", views.DealCreate.as_view(), name = "deal_new"),
    path("deals/closedate", views.DealbyCloseDate.as_view(), name = "deal_byclosedate"),
    path("deals/status", views.DealbyStatus.as_view(), name = "deal_bystatus"),

]