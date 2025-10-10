from django.shortcuts import render, get_object_or_404
from django.http import Http404
from contact.models import Contacts

# Create your views here.

def index(request):
    contacts = Contacts.objects.filter(show=True).order_by('id')

    context = {
        "contacts" : contacts,
    }
    return render(
        request,
        'contact/index.html',
        context = context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contacts.objects.filter(pk=contact_id, show=True))

    context = {
        'contact' : single_contact
    }

    return render(
        request,
        'contact/contact.html',
        context = context
    )