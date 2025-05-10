from django.contrib import admin
from .models import Hospital, Review

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'business_hours']  # ✅ 운영시간 표시
    search_fields = ['name', 'address']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'author', 'rating', 'created_at']
    search_fields = ['hospital__name', 'author']
