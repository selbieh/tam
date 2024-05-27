from django.urls import path

from .views import CreateContactView, ContactDetailView, ListContactView, PhoneNumberCreateView

app_name = "contacts"

urlpatterns = [
    path("", ListContactView.as_view(), name="contact_list"),
    path("create/", CreateContactView.as_view(), name="contact_create"),
    path("<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
    path("<int:pk>/phonenumber/create/", PhoneNumberCreateView.as_view(), name="phone_number_create"),
]
