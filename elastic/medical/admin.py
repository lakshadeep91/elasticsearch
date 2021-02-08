from django.contrib import admin

# Register your models here.

from .models import Seller, Product, Inventory


class SellerAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class InventoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
