from django.contrib import admin
from market.models import Category, Product
# , Order, OrderProduct, Store, Provider, Consumer,


# class ProviderAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Provider, ProviderAdmin)
#
#
# class ConsumerAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Consumer, ConsumerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)


# class OrderAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Order, OrderAdmin)
#
#
# class OrderProductAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(OrderProduct, OrderProductAdmin)
#
#
# class StoreAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Store, StoreAdmin)