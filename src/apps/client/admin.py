from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from .models import Company, Product

admin.site.register(Company, SingletonModelAdmin)


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ['productName', 'productType', 'productCost']
    list_filter = ['created', 'updated']
    search_fields = ['productName', 'productType', 'productCost']
