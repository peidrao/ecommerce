from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from carts.models import CartItem
from category.models import Category

from store.models import Product

from carts.views import _cart_id
# Create your views here.


def store(request, category_slug: str = None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    context = {
        'products': paged_products,
        'count': products_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug: str = None, product_slug: str = None):
    try:
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=product).exists()
    except Product.DoesNotExist:
        product = None

    context = {
        'product': product,
        'in_cart': in_cart
    }
    return render(request, 'store/product_detail.html', context)
