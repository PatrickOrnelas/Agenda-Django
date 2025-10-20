from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contacts
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

class ContactsForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome'
            }
        ),
        label='Primeiro Nome',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu sobrenome'
            }
        ),
        label='Sobrenome',
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu telefone'
            }
        ),
        label='Telefone',
    )

    class Meta:
        model = Contacts
        fields = ('first_name', 'last_name', 'phone',)
        widgets = {
            'first_name' : forms.TextInput(
                attrs= {
                    'placeholder' : 'Teste'
                }
            )
        }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        return super().clean()
