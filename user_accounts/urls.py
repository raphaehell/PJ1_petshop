from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile, name="profile"),
    path("", views.user_accounts_main, name="user_accounts_main"),
]