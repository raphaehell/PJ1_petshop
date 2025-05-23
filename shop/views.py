# PJ1/shop/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Product # Category와 Product 모델 임포트

# 상품 목록 뷰
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all() # 모든 카테고리
    products = Product.objects.filter(available=True) # 판매 가능한 상품만 가져오기

    if category_slug:
        # 특정 카테고리 선택 시 해당 카테고리와 상품 필터링
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product_list.html', context)

# 상품 상세 뷰
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)