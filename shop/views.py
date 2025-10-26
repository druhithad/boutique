from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})

def product_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), available=True)
    return render(request, 'shop/product_search.html', {'query': query, 'results': results})
