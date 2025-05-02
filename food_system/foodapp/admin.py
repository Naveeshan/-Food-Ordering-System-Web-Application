from django.contrib import admin

from foodapp.models import User,MenuItem,Order

admin.site.register(User)
from django.contrib import admin
from .models import MenuItem, Order

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')   # Only valid fields
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'menu_item', 'quantity', 'order_time')  # Only valid fields
    search_fields = ('customer_name',)
    list_filter = ('order_time',)
