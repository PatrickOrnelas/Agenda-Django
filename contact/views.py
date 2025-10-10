from django.shortcuts import render
from contact.models import Contacts

# Create your views here.

def index(request):
    contacts = Contacts.objects.all()

    context = {
        "contacts" : contacts,
    }
    return render(
        request,
        'contact/index.html',
        context = context
    )