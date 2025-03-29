from django.contrib import admin
from django.urls import path, include  # include 함수 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),  # account 앱의 urls.py 파일 포함
    # ... 다른 URL 패턴 ...
]