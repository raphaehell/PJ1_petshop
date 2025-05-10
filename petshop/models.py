from django.db import models

class Hospital(models.Model):
    kakao_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)
    
    business_hours = models.CharField(max_length=200, blank=True)  # ✅ 운영시간 필드 추가

    def __str__(self):
        return self.name

class Review(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)  # 나중에 유저 연동하면 바꿔도 됨
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()  # 1~5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.hospital.name}] {self.rating}점 by {self.author}"
