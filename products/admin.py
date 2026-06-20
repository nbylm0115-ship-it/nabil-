from django.contrib import admin

from .models import Product, Order, OrderItem


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        'product',
        'size',
        'color',
        'quantity',
        'price',
    )


class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'total_price',
        'created_at',
    )

    inlines = [OrderItemInline]


admin.site.register(Product)

admin.site.register(Order, OrderAdmin)