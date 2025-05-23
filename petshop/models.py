# PJ1/petshop/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() # Django의 기본 User 모델을 가져옴

class Hospital(models.Model):
    # Kakao API에서 받아온 정보
    kakao_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    place_name = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address_name = models.CharField(max_length=255)
    road_address_name = models.CharField(max_length=255, null=True, blank=True)
    x = models.CharField(max_length=50) # 경도
    y = models.CharField(max_length=50) # 위도
    place_url = models.URLField(max_length=500)

    # 추가 정보 (필요시 사용)
    opening_hours = models.CharField(max_length=255, null=True, blank=True) # 영업시간
    # rating = models.FloatField(null=True, blank=True) # 카카오 평점이 있다면 사용

    def __str__(self):
        return self.place_name

    def get_average_rating(self):
        # 이 병원에 대한 모든 리뷰의 평점을 가져와 평균 계산
        reviews = self.reviews.all() # related_name='reviews' 사용
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return round(total_rating / reviews.count(), 2)
        return None # 리뷰가 없으면 None 반환

class Review(models.Model):
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="reviews"
    )
    # user 필드를 nullable하게 변경하고, related_name 추가
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='petshop_reviews')
    content = models.TextField()
    rating = models.IntegerField(default=0, help_text="1에서 5까지의 평점 (별점)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass # 특별한 Meta 옵션이 없으면 비워둬도 됨.

    def __str__(self):
        # user가 null일 경우를 대비하여 처리
        if self.user:
            return f"{self.user.username} - {self.hospital.place_name} ({self.rating}점)"
        else:
            return f"익명 사용자 - {self.hospital.place_name} ({self.rating}점)"