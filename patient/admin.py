from django.contrib import admin

# Register your models here.
from .models import Patient, logs

admin.site.register(Patient)
admin.site.register(logs)