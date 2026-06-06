from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order, OrderItem


# HOME PAGE
def home(request):

    products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


# PRODUCT DETAILS
def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    return render(request, 'product.html', {
        'product': product
    })


# ADD TO CART
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    size = request.GET.get('size', '')
    color = request.GET.get('color', '')

    cart = request.session.get('cart', {})

    key = f"{id}_{size}_{color}"

    if key in cart:

        cart[key]['quantity'] += 1

    else:

        cart[key] = {
            'id': product.id,
            'quantity': 1,
            'size': size,
            'color': color,
        }

    request.session['cart'] = cart

    return redirect('cart')


# CART PAGE
def cart(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    for key, item in cart.items():

        product_id = item.get('id')

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            continue

        quantity = item['quantity']
        size = item.get('size')
        color = item.get('color')

        subtotal = product.price * quantity

        total += subtotal

        items.append({
            'key': key,
            'product': product,
            'quantity': quantity,
            'size': size,
            'color': color,
            'subtotal': subtotal,
        })

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


# INCREASE QUANTITY
def increase_quantity(request, key):

    cart = request.session.get('cart', {})

    if key in cart:

        cart[key]['quantity'] += 1

    request.session['cart'] = cart

    return redirect('cart')


# DECREASE QUANTITY
def decrease_quantity(request, key):

    cart = request.session.get('cart', {})

    if key in cart:

        if cart[key]['quantity'] > 1:

            cart[key]['quantity'] -= 1

        else:

            del cart[key]

    request.session['cart'] = cart

    return redirect('cart')


# REMOVE ITEM
def remove_item(request, key):

    cart = request.session.get('cart', {})

    if key in cart:

        del cart[key]

    request.session['cart'] = cart

    return redirect('cart')


# CHECKOUT
def checkout(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    for key, item in cart.items():

        product_id = item.get('id')

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            continue

        quantity = item['quantity']
        size = item.get('size')
        color = item.get('color')

        subtotal = product.price * quantity

        total += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'size': size,
            'color': color,
            'subtotal': subtotal,
        })

    if request.method == 'POST':

        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        payment_screenshot = request.FILES.get('payment_screenshot')

        order = Order.objects.create(
            full_name=name,
            phone=phone,
            address=address,
            total_price=total,
            payment_screenshot=payment_screenshot
    )

        for item in items:

           OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['subtotal'],
                size=item['size'],
                color=item['color'],
        )

        request.session['cart'] = {}

        return redirect('success')

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })


# SUCCESS PAGE
def success(request):

    return render(request, 'success.html')

from django.shortcuts import render

def men(request):
    products = Product.objects.filter(category='men')

    return render(
        request,
        'products/men.html',
        {
            'products': products
        }
    )


def women(request):
    products = Product.objects.filter(category='women')

    return render(
        request,
        'products/women.html',
        {
            'products': products
        }
    )


def classic(request):
    products = Product.objects.filter(category='classic')

    return render(
        request,
        'products/classic.html',
        {
            'products': products
        }
    )