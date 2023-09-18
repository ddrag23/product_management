from django.contrib import admin
from .models import Product,Satuan,Status

# Register your models here.
admin.site.register([Status,Satuan,Product])