from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contacts
from django.core.paginator import Paginator
from django import forms
from contact.forms import ContactsForm, RegisterForm
from django.urls import reverse

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
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactsForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,

        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactsForm(),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )

def update(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactsForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,

        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactsForm(instance=contact),
        'form_action': form_action
    }

    return render(
        request,
        'contact/create.html',
        context
    )

def delete(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(request, 'contact/contact.html', {
        'contact': contact,
        'confirmation' : confirmation, 
    })

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,
                  'contact/register.html',
                  {
                      'form' : form,
                  }
                  )