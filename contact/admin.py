from django.contrib import admin
from contact import models

@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id', 
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 25
    list_max_show_all = 100
    # list_editable = 'first_name', 'last_name'