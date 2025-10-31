from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contacts
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactsForm
# Create your views here.

def index(request):
    contacts = Contacts.objects.filter(show=True).order_by('id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj" : page_obj,
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
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj" : page_obj,
        "site_title": '- Busca',
        'search_value': search_value,
    }
    return render(
        request,
        'contact/index.html',
        context = context
    )

def create(request):


    if request.method == 'POST':
        form = ContactsForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactsForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )