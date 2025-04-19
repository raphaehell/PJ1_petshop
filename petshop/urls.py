from django.urls import path
from . import views

urlpatterns = [
    # path('test-kakao/', views.test_kakao, name='test_kakao'),  ← 요거 주석 처리하거나 삭제
    path('find-places/', views.find_places_view, name='find_places'),
    path('map/', views.map_test, name='map_test'),
    path('submit-review/', views.submit_review, name='submit_review'),
]
