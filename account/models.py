from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 추가 필드 정의 (예: 전화번호, 생일 등)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 주소 관련 필드 정의 (예: 우편번호, 주소, 상세 주소 등)