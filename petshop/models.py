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

class running(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='running')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20)  # 예: 'running', 'completed', 'canceled'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.hospital.name}] {self.status} from {self.start_time} to {self.end_time}"
    
    
class dogtype(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    weight = models
    sex = models.CharField(max_length=10)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='dogtype')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.breed}) - {self.age} years old"
    def __str__(self):
        return f"{self.name} ({self.breed}) - {self.age} years old"
    def __str__(self):
        return f"{self.name} ({self.breed}) - {self.age} years old"
# 중성화 여부/백신 여부/예방접종 여부/어떤 백신인지/특이사항 추가 필요