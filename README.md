# PJ1_PetShop

반려동물 용품 쇼핑몰 프로젝트입니다.

## 프로젝트 설명

본 프로젝트는 반려견 용품을 판매하는 온라인 쇼핑몰입니다. 사용자들은 다양한 상품을 검색하고 구매할 수 있으며, 관리자는 상품 및 주문 관리를 할 수 있습니다.

## 설치 방법

1.  가상 환경 생성:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  의존성 라이브러리 설치:

    ```bash
    pip install -r requirements.txt
    ```

3.  데이터베이스 설정:

    * MySQL 데이터베이스를 생성하고 설정 파일(settings.py)에 데이터베이스 정보를 입력합니다.

4.  데이터베이스 마이그레이션:

    ```bash
    python manage.py migrate
    ```

## 실행 방법

```bash
python manage.py runserver
