# PJ1/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # allauth URL
    path('user_accounts/', include('user_accounts.urls')), # user_accounts 앱 URL
    path('vet/', include('petshop.urls')), # vet 앱 URL
    path('shop/', include('shop.urls')),
    # 필요하다면 다른 앱의 URL도 여기에 추가
]