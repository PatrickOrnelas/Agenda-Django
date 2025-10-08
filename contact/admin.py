from django.contrib import admin
from contact import models

@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    pass