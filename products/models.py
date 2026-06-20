from django.db import models
from django.utils import timezone


# =========================================
# PRODUCT
# =========================================

class Product(models.Model):

    name = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='products/'
    )

    black_image = models.ImageField(upload_to='products/', blank=True, null=True)
    white_image = models.ImageField(upload_to='products/', blank=True, null=True)
    grey_image = models.ImageField(upload_to='products/', blank=True, null=True)
    brown_image = models.ImageField(upload_to='products/', blank=True, null=True)
    beige_image = models.ImageField(upload_to='products/', blank=True, null=True)
    olive_image = models.ImageField(upload_to='products/', blank=True, null=True)

    black_stock = models.IntegerField(default=0)
    white_stock = models.IntegerField(default=0)
    grey_stock = models.IntegerField(default=0)
    brown_stock = models.IntegerField(default=0)
    beige_stock = models.IntegerField(default=0)
    olive_stock = models.IntegerField(default=0)

    CATEGORY_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('classic', 'Classic'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='men'
    )

    stock = models.IntegerField(default=1)

    created_at = models.DateTimeField(
    default=timezone.now
)

def __str__(self):
        return self.name


# =========================================
# CART
# =========================================

class Cart(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Cart {self.id}"


# =========================================
# CART ITEM
# =========================================

class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    size = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def subtotal(self):

        return self.product.price * self.quantity

    def __str__(self):

        return self.product.name


# =========================================
# ORDER
# =========================================

class Order(models.Model):

    PAYMENT_CHOICES = [

        ('cash', 'Cash On Delivery'),

        ('instapay', 'Instapay'),

        ('vodafone', 'Vodafone Cash'),

    ]

    full_name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_CHOICES,
        default='cash'
    )

    payment_screenshot = models.ImageField(
        upload_to='payments/',
        blank=True,
        null=True
    )

    shipping_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=70
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.full_name


# =========================================
# ORDER ITEM
# =========================================

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    size = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def subtotal(self):

        return self.price * self.quantity

    def __str__(self):

        return f"{self.product.name} x {self.quantity}"