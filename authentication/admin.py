import imp
from pydoc import Doc
from telnetlib import DO
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Normal, NGO, Doctor

admin.site.register(User, UserAdmin)
admin.site.register(NGO)
admin.site.register(Normal)
admin.site.register(Doctor)

# Register your models here.
