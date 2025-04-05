# Generated by Django 5.0 on 2024-01-22 18:23
import random

from django.db import migrations

from restaurant_app.models import Restaurant


def add_restaurant_data(apps, schema_editor):
    # 레스토랑 데이터 생성을 위한 샘플 리스트
    restaurant_names = [
        'BBQ 치킨', '페리카나', '고갯마루', '불고기브라더스', '청하오리',
        '비빔밥천국', '봉구스 밥버거', '신선설농탕', '왕비집', '토담골',
        '풍년집', '진짜루', '늘솜', '배꼽집', '한라갈비',
        '찜닭의 전설', '순남시래기', '명랑시대', '깐부치킨', '소문난 주먹밥',
        '최고집', '밥을 먹자', '매화', '숯불집', '오늘도 떡볶이',
        '설빙', '빽다방', '할매순대국', '아구찜 전문점', '양푼이 미역국',
        '옛날국수', '쌀통닭', '우리집 감자탕', '춘천닭갈비', '만두의 신',
        '떡보의 비밀', '곱창대왕', '쭈꾸미 브라더스', '모둠전 전문점', '오떡오떡',
        '전주비빔밥', '영덕대게', '한우마을', '서울김밥', '백종원의 포장마차',
        '킹덤 탕수육', '스시도', '동태찌개 전문', '강남면옥', '홍루이젠'
    ]

    addresses = [
        '서울시 강남구', '서울시 강동구', '서울시 강서구', '서울시 강북구', '서울시 서초구',
        '서울시 송파구', '서울시 도봉구', '서울시 노원구', '서울시 은평구', '서울시 중랑구'
    ]

    phone_numbers = [f'02-1234-{i:04}' for i in range(9000, 9050)]
    ratings = [random.randint(3, 5) for _ in range(50)]
    menus = [
        '치킨', '불고기', '해물찜', '비빔밥', '순대국',
        '돈까스', '떡볶이', '갈비', '탕수육', '김밥'
    ]

    restaurants = []

    for i in range(50):
        restaurant = {
            'name': restaurant_names[i],
            'address': random.choice(addresses),
            'phone': phone_numbers[i],
            'rating': ratings[i],
            'menu': random.choice(menus),
            'image': ''  # 빈 이미지 경로; 실제 이미지 경로가 필요한 경우 채워넣을 수 있습니다.
        }
        restaurants.append(restaurant)

    Restaurant.objects.bulk_create([
        Restaurant(
            name=r['name'],
            address=r['address'],
            phone=r['phone'],
            latitude=37.5665,
            longitude=126.9780,
            rating=r['rating'],
        ) for r in restaurants
    ])

def reverse_add_restaurant_data(apps, schema_editor):
    Restaurant = apps.get_model('restaurant', 'Restaurant')
    Restaurant.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_restaurant_data, reverse_code=reverse_add_restaurant_data),
    ]