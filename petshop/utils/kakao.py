import requests
from django.conf import settings

def search_places_by_keyword(query, x, y, radius=5000):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {
        "Authorization": f"KakaoAK {settings.KAKAO_API_KEY}",  # REST API 키
    }
    params = {
        "query": query,
        "x": x,
        "y": y,
        "radius": radius,
    }

    response = requests.get(url, headers=headers, params=params)

    try:
        data = response.json()
    except ValueError:
        return {"error": "Invalid JSON response from Kakao"}

    if response.status_code != 200:
        return {
            "error": "Kakao API request failed",
            "status_code": response.status_code,
            "detail": data,
        }

    documents = data.get("documents", [])
    
    # ✅ '운영시간' 필드 기본값 추가
    for place in documents:
        place['business_hours'] = "정보 없음"  # 또는 "카카오 장소 페이지 참조"

    return documents
