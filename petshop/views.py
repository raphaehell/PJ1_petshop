# petshop/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Hospital, Review # Hospital과 Review 모델 import
from .utils.kakao import search_places_by_keyword
from django.conf import settings
import json
from django.db.models import Avg # Avg 함수 import (평균 계산용)

@ensure_csrf_cookie
def map_test(request):
    return render(request, 'map_test.html', {
        'KAKAO_JAVASCRIPT_KEY': settings.KAKAO_JAVASCRIPT_KEY
    })

def find_places_view(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            x = body.get("longitude")
            y = body.get("latitude")
            query = body.get("query", "동물병원")

            if not x or not y:
                print("find_places_view: Missing longitude or latitude.")
                return JsonResponse({'error': '위치 정보가 없습니다.'}, status=400)

            results = search_places_by_keyword(query, x, y)

            if isinstance(results, dict) and 'error' in results:
                print(f"find_places_view: Kakao API Error from utils: {results['error']}")
                return JsonResponse(results, status=500) 

            if not results:
                print("find_places_view: No search results found.")
                return JsonResponse({'message': '검색 결과가 없습니다.'}, safe=False)

            simplified_results = []
            for place in results:
                place_name = place.get('place_name')
                
                # 평균 평점 계산 로직 추가 시작
                # 카카오 API 결과의 place_name과 일치하는 Hospital 객체 찾기
                hospital_obj = Hospital.objects.filter(name=place_name).first()
                
                average_rating = None
                if hospital_obj:
                    # 해당 병원에 대한 리뷰들의 평점 평균 계산
                    # aggregate 함수로 'rating' 필드의 평균을 구하고, rating__avg로 접근
                    avg_data = Review.objects.filter(hospital=hospital_obj).aggregate(Avg('rating'))
                    if avg_data['rating__avg'] is not None:
                        average_rating = round(avg_data['rating__avg'], 1) # 소수점 첫째자리까지 반올림
                # 평균 평점 계산 로직 추가 끝
                # -----------------------------------------------------

                simplified_results.append({
                    'place_name': place_name,
                    'address_name': place.get('address_name'),
                    'phone': place.get('phone'),
                    'place_url': place.get('place_url'),
                    'distance': place.get('distance'),
                    'x': place.get('x'),
                    'y': place.get('y'),
                    'average_rating': average_rating, # 계산된 평균 평점 추가
                    'opening_hours': "정보 없음", # (아직 구현 안됨)
                    'image_url': "https://via.placeholder.com/150" # (아직 구현 안됨)
                })
            
            print(f"find_places_view: Found {len(simplified_results)} places with ratings.")
            return JsonResponse(simplified_results, safe=False)

        except json.JSONDecodeError:
            print("find_places_view: Invalid JSON format in request body.")
            return JsonResponse({'error': '잘못된 JSON 형식입니다.'}, status=400)
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f"find_places_view: An unexpected error occurred during POST request processing: {e}")
            return JsonResponse({'error': '서버 처리 중 예상치 못한 오류 발생', 'detail': str(e)}, status=500)
    else:
        print("find_places_view: Only POST requests are allowed for this endpoint.")
        return JsonResponse({'error': 'POST 요청만 허용됩니다.'}, status=400)

def submit_review(request):
    
    pass