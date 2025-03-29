from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # 다른 URL 패턴 추가
]