from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile, name="profile"),  # 프로필 페이지 URL 추가
]