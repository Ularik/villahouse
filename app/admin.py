from django.contrib import admin
from .models import House, Category, MethodPayment, Storage


admin.site.register(House)
admin.site.register(Category)
admin.site.register(MethodPayment)
admin.site.register(Storage)