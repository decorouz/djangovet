from django.contrib import admin

# Register your models here.

from .models import Owner, Patient

admin.site.register(Owner)
admin.site.register(Patient)
