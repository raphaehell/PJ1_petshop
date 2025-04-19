# petshop/utils/kakao.py

import requests
from django.conf import settings

def search_places_by_keyword(query, x, y, radius=5000):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {
        "Authorization": f"KakaoAK {settings.KAKAO_API_KEY}",  # 또는 KAKAO_REST_API_KEY
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

    return data.get("documents", [])

    print(response.json())

    print(f"[DEBUG] Kakao API Key: {settings.KAKAO_API_KEY}")