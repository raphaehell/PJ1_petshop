import requests
import json
from django.conf import settings

def search_places_by_keyword(query, x, y, radius=2000): # x=longitude, y=latitude
    """
    카카오 로컬 API를 사용하여 키워드 기반으로 장소를 검색합니다.
    """
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    
    try:
        # settings.KAKAO_REST_API_KEY가 있는지 확인하는 로직 추가
        # hasattr로 속성 존재 여부를 확인하고, 값이 비어있는지도 체크
        if not hasattr(settings, 'KAKAO_REST_API_KEY') or not settings.KAKAO_REST_API_KEY:
            error_msg = "KAKAO_REST_API_KEY가 settings.py에 설정되지 않았거나 비어있습니다."
            print(f"설정 오류: {error_msg}")
            # 이 경우 클라이언트에게 에러 딕셔너리를 반환
            return {'error': error_msg}

        # settings에서 직접 키를 가져와 사용
        headers = {"Authorization": f"KakaoAK {settings.KAKAO_REST_API_KEY}"} 

        params = {
            "query": query,
            "x": x, # 경도
            "y": y, # 위도
            "radius": radius, # 검색 반경 (단위: 미터), 기본 2km
            "category_group_code": "HP8", # HP8: 병원 (동물병원을 명시적으로 검색하지 않아도 이 그룹 코드가 병원을 포함할 수 있음)
                                          # 특정 카테고리가 없다면 이 필드를 제거할 수도 있음
            "size": 15 # 한 페이지에 보여질 문서 수, 최대 15
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() # HTTP 오류가 발생하면 예외 발생 (2xx 상태 코드가 아니면)

        data = response.json()
        return data.get('documents', []) # 'documents' 리스트를 반환. 없으면 빈 리스트 반환

    except requests.exceptions.HTTPError as e: # HTTP 상태 코드 4xx, 5xx 에러 (requests.raise_for_status()에 의해 발생)
        error_msg = f"Kakao API HTTP 오류 (상태코드: {e.response.status_code}): {e.response.text}"
        print(error_msg)
        return {'error': error_msg}
    except requests.exceptions.RequestException as e: # 네트워크 연결, DNS 문제 등 request 라이브러리 관련 모든 에러
        error_msg = f"Kakao API 호출 중 네트워크 또는 요청 오류: {e}"
        print(error_msg)
        return {'error': error_msg}
    except json.JSONDecodeError as e: # 서버 응답이 JSON 형식이 아닐 때 발생하는 에러
        error_msg = f"Kakao API 응답 JSON 파싱 오류: {e}"
        print(error_msg)
        return {'error': error_msg}
    except Exception as e: # 위에 명시되지 않은 모든 예상치 못한 다른 종류의 에러
        error_msg = f"search_places_by_keyword 함수에서 예상치 못한 오류 발생: {e}"
        print(error_msg)
        return {'error': error_msg}