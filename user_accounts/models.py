# user_accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    전화번호 = models.CharField(max_length=20, blank=True)
    생일 = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    우편번호 = models.CharField(max_length=10, blank=True)
    주소 = models.CharField(max_length=255, blank=True)
    상세주소 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.주소}'