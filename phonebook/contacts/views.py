from django.db import transaction
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from .forms import PhoneNumberForm, PhoneNumberFormSet
from .models import Contact, PhoneNumber


class CreateContactView(CreateView):
    model = Contact
    fields = ["name"]
    template_name = "contacts/contact_form.html"
    success_url = reverse_lazy("contacts:contact_list")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["phone_numbers"] = PhoneNumberFormSet(self.request.POST)
        else:
            data["phone_numbers"] = PhoneNumberFormSet()
        return data

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        context = self.get_context_data()
        phone_numbers = context["phone_numbers"]
        with transaction.atomic():
            self.object = form.save()
            if phone_numbers.is_valid():
                phone_numbers.instance = self.object
                phone_numbers.save()
        return super().form_valid(form)


class PhoneNumberCreateView(CreateView):
    model = PhoneNumber
    form_class = PhoneNumberForm
    template_name = "contacts/phone_number_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact"] = Contact.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.contact = Contact.objects.get(pk=self.kwargs["pk"])
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse("contacts:contact_detail", args=[self.object.contact.pk])


class ListContactView(ListView):
    model = Contact
    template_name = "contacts/contact_list.html"
    context_object_name = "contacts"
    paginate_by = 10  # Number of contacts per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = context['contacts']
        paginator = Paginator(contacts, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

class ContactDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_detail.html"
    context_object_name = "contact"
