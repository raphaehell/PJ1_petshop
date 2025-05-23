# petshop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('find-places/', views.find_places_view, name='find_places'), # 주변 병원 검색 API
    path('map/', views.map_test, name='map_test'), # 지도 페이지
    path('submit-review/', views.submit_review, name='submit_review'), # 리뷰 제출 API
    # 여기에 다른 petshop 관련 URL들을 추가할 수 있습니다.
]