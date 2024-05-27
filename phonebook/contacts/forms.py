from django import forms

from .models import Contact, PhoneNumber


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name"]


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ["number"]


PhoneNumberFormSet = forms.modelformset_factory(PhoneNumber, form=PhoneNumberForm, extra=1)
