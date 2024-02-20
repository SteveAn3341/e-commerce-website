
from django.shortcuts import render, get_object_or_404 , redirect
from shooping_cart.models import Product 
from .cart import Cart

def home(request):
    return render(request, 'pages/home.html')

def category(request, category_id):
    products = Product.objects.filter(category=category_id)
    return render(request, 'pages/category.html', {'products': products})

def product(request):
    products = Product.objects.all()
    print(products) 
    return render(request, 'pages/product.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/product_detail.html', {'product': product})

def personal_use(request):
    products = Product.objects.filter(category__name='Personal Use')
    return render(request, 'pages/personal_use.html', {'products': products})

def office_use(request):
    products = Product.objects.filter(category__name='Office Use')
    return render(request, 'pages/office_use.html', {'products': products})

def home_use(request):
    products = Product.objects.filter(category__name='Home Use')
    return render(request, 'pages/home_use.html', {'products': products})

def add_to_cart(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('shopping_cart')

def shopping_cart(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'pages/shopping_cart.html', context)

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shopping_cart')