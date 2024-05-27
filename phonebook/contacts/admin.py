# Register your models here.
from django.contrib import admin

from .models import Contact, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [PhoneNumberInline]


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ["number", "contact"]
