from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    전화번호 = models.CharField(max_length=20, blank=True)
    생일 = models.DateField(null=True, blank=True)
    # 필요한 다른 필드들을 추가하세요.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    우편번호 = models.CharField(max_length=10, blank=True)
    주소 = models.CharField(max_length=255, blank=True)
    상세주소 = models.CharField(max_length=255, blank=True)
    # 필요한 다른 필드들을 추가하세요.