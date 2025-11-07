from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contacts, Category
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'placeholder': 'Digite seu email'
            }
        ),
        label='Email',
        required=False,
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Digite uma descrição',
                'rows': 5,
                'cols': 20
            }
        ),
        label='Descrição',
        required=False,
    )

    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        empty_label = 'Selecione a categoria',
        label='Categoria',
        required=False,
    )

    picture = forms.ImageField(
        label='Foto',
        required=False,
        widget=forms.FileInput(
            attrs = {
                'accept' : 'image/*'
            }
        ),
    )

    class Meta:
        model = Contacts
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')
   

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
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label='Primeiro Nome'
    )
    last_name = forms.CharField(
        required=True,
        label='Sobrenome'
    )
    email = forms.EmailField(
        required=True,
        label='Email'
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Email já cadastrado.', code='invalid'))
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatório',
        label='Primeiro Nome',
        error_messages={
            'min_length': 'O primeiro nome deve ter no mínimo 2 caracteres.',
            'max_length': 'O primeiro nome deve ter no máximo 30 caracteres.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatório',
        label='Sobrenome',
        error_messages={
            'min_length': 'O sobrenome deve ter no mínimo 2 caracteres.',
            'max_length': 'O sobrenome deve ter no máximo 30 caracteres.'
        }
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Confirmação de Senha',
        widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password'}),
        strip=False,
        help_text='Digite a mesma senha para verificação.',
        required=False,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)

    def save(self, commit = True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('As senhas não coincidem.', code='invalid')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error('email', ValidationError('Email já cadastrado.', code='invalid'))
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', errors)

        return password1