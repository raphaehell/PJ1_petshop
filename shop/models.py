# PJ1/shop/models.py

from django.db import models
from django.db.models import Index # Index 클래스 임포트 확인

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # URL에 사용될 고유 이름

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories' # 관리자 페이지에서 보여질 이름

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True) # URL에 사용될 고유 이름
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # 상품 사진 (pip install Pillow 필요)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # 소수점 포함 가격
    stock = models.PositiveIntegerField() # 재고
    available = models.BooleanField(default=True) # 판매 중 여부
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        # index_together 대신 indexes 사용
        indexes = [
            Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.name