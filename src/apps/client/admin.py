from django.contrib import admin
from solo.admin import SingletonModelAdmin

# Register your models here.
from .models import Company, Product, Order

admin.site.register(Company, SingletonModelAdmin)


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ['productName', 'productType', 'productCost']
    list_filter = ['created', 'updated']
    search_fields = ['productName', 'productType', 'productCost']


@admin.register(Order)
class Admin(admin.ModelAdmin):
    list_display = ['order_id', 'product', 'shop', 'due_date', 'quantity']
    list_filter = ['created', 'updated']
    search_fields = ['product', 'shop', 'due_date']
