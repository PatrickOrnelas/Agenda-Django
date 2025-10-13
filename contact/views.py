from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import Http404
from contact.models import Contacts

# Create your views here.

def index(request):
    contacts = Contacts.objects.filter(show=True).order_by('id')[0:10]

    context = {
        "contacts" : contacts,
        "site_title": '- Contatos'
    }
    return render(
        request,
        'contact/index.html',
        context = context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contacts.objects.filter(pk=contact_id, show=True))

    site_title = f' - {single_contact.first_name + ' ' + single_contact.last_name} '

    context = {
        'contact' : single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context = context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contacts.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) | 
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) ).order_by('id')

    context = {
        "contacts" : contacts,
        "site_title": '- Busca',
        'search_value': search_value,
    }
    return render(
        request,
        'contact/index.html',
        context = context
    )