from django.contrib import admin
from posApp.models import Category, Products, Sales, salesItems

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'date_added', 'date_updated']
    list_filter = ['status']
    search_fields = ['name', 'description']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category_id', 'price', 'status', 'date_added', 'date_updated']
    list_filter = ['category_id', 'status']
    search_fields = ['code', 'name', 'description']

class SalesItemsInline(admin.TabularInline):
    model = salesItems
    extra = 1

class SalesAdmin(admin.ModelAdmin):
    list_display = ['code', 'sub_total', 'grand_total', 'tax_amount', 'date_added', 'date_updated']
    search_fields = ['code']
    inlines = [SalesItemsInline]

class SalesItemsAdmin(admin.ModelAdmin):
    list_display = ['sale_id', 'product_id', 'price', 'qty', 'total']
    list_filter = ['sale_id', 'product_id']
    search_fields = ['sale_id__code', 'product_id__name']

# Register your models with the custom admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(salesItems, SalesItemsAdmin)