from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Hospital, Review
from .utils.kakao import search_places_by_keyword
from django.conf import settings
import json

# 지도 페이지 렌더링 (CSRF 토큰 보장 및 KAKAO API 키 전달)
@ensure_csrf_cookie
def map_test(request):
    return render(request, 'map_test.html', {
        'KAKAO_API_KEY': settings.KAKAO_API_KEY
    })


# 병원 정보 및 리뷰 데이터 반환
def find_places_view(request):
    if request.method == "POST":
        body = json.loads(request.body)
        x = body.get("longitude")
        y = body.get("latitude")
        query = "동물병원"

        results = search_places_by_keyword(query, x, y)
        simplified_results = []

        for place in results:
            kakao_id = place['id']

            # DB에 병원 정보 없으면 생성
            hospital, created = Hospital.objects.get_or_create(
                kakao_id=kakao_id,
                defaults={
                    'name': place['place_name'],
                    'address': place['address_name'],
                    'phone': place.get('phone', ''),
                    'url': place.get('place_url', ''),
                    'x': place['x'],
                    'y': place['y'],
                }
            )

            reviews = hospital.reviews.all()
            avg_rating = round(sum(r.rating for r in reviews) / reviews.count(), 1) if reviews.exists() else None

            simplified_results.append({
                'place_name': hospital.name,
                'address_name': hospital.address,
                'phone': hospital.phone or '번호 없음',
                'place_url': hospital.url,
                'x': hospital.x,
                'y': hospital.y,
                'kakao_place_id': hospital.kakao_id,
                'avg_rating': avg_rating,
                'review_count': reviews.count(),
            })

        return JsonResponse(simplified_results, safe=False)
    else:
        return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=400)


# 리뷰 등록 처리
def submit_review(request):
    if request.method == "POST":
        data = json.loads(request.body)

        kakao_id = data.get('kakao_place_id')
        rating = data.get('rating')
        comment = data.get('comment')

        if not all([kakao_id, rating, comment]):
            return JsonResponse({"error": "모든 필드를 입력해야 합니다."}, status=400)

        hospital = get_object_or_404(Hospital, kakao_id=kakao_id)

        Review.objects.create(
            hospital=hospital,
            author="익명",  # 향후 로그인 유저 연동
            rating=int(rating),
            content=comment
        )

        return JsonResponse({"message": "리뷰 등록 완료!"})
    else:
        return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=400)
### 후 협업할  떄 사용해서 개인 프젝으로 진행
