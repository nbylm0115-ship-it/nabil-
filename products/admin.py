from django.contrib import admin
from .models import Product, Order, OrderItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'price',
        'category',
        'stock',
    )

    fieldsets = (

        ('Basic Info', {
            'fields': (
                'name',
                'price',
                'description',
                'category',
                'stock',
            )
        }),

        ('Main Image', {
            'fields': (
                'image',
            )
        }),

        ('Color Images', {
            'fields': (
                'black_image',
                'white_image',
                'grey_image',
                'brown_image',
                'beige_image',
                'olive_image',
            )
        }),

        ('Color Stock', {
            'fields': (
                'black_stock',
                'white_stock',
                'grey_stock',
                'brown_stock',
                'beige_stock',
                'olive_stock',
            )
        }),
    )


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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'phone',
        'total_price',
        'created_at',
    )

    inlines = [OrderItemInline]