from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactList.as_view(), name="contact_list"),
    path("contacts/lastcontacted", views.ContactsNeedUpdate.as_view(), name = "contact_lastcontacted"),
    path("contacts/contactbycompany", views.ContactsByCompany.as_view(), name = "contact_bycompany"),
    path("contacts/<int:pk>/", views.ContactDetail.as_view(), name = "contactdetail"),
    path("contacts/<int:pk>/edit", views.ContactEdit.as_view(), name = "contactedit"),
    path("contacts/<int:pk>/delete", views.ContactDelete.as_view(), name = "contact_delete"),
    path("contacts/new", views.ContactCreate.as_view(), name = "contact_new"),


]