from django.shortcuts import render, get_object_or_404
from .models import Category , Product , Bestseller
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def index(request):
    return render(request, 'home.html')

def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id= category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'shop/catagory.html',{'category':category, 'prods':products})

    paginator = Paginator(products, 6)
    try:
        page = int(request.Get.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product':product})

def bestseller(request,product_id=None):
    bestseller = Bestseller.objects.filter(available=True)
    products = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/bestseller.html', {'bestseller':bestseller , 'prods':products})