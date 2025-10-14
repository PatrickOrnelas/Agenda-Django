from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contacts
from django.core.paginator import Paginator
from django import forms

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('first_name', 'last_name', 'phone',)
