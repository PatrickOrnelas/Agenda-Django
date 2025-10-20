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
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo.',
                    code='invalid'
                )

        if first_name == last_name:
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError('Não digite ABC neste campo.',
                code='invalid')
            )
        return first_name