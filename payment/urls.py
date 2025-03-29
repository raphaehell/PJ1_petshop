from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls')),  # payment 앱의 urls.py 파일 포함
    # ...
]