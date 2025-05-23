# PJ1/shop/urls.py

from django.urls import path
from . import views

app_name = 'shop' # 앱의 네임스페이스 지정

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]