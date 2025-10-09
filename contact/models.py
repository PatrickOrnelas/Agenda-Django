from django.db import models
from django.utils import timezone

"""
Table Contacts:
    id(primary key - AUTO),
    first_name(string),
    last_name(string - blank=True),
    phone(string),
    email(email, blank=True),
    created_date(date),
    description(text)

DEPOIS:
    owner(foreign key),

"""
