from django.contrib import admin
from .models import ContactUs, ContactUsRequest

admin.site.register(ContactUsRequest)
admin.site.register(ContactUs)
