from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Referdata, New_patient

admin.site.register(Referdata)
admin.site.register(New_patient)