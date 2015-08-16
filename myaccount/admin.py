from django.contrib import admin

from .models import productCategory, orderStatus

# Register your models here.
admin.site.register(productCategory)
admin.site.register(orderStatus)