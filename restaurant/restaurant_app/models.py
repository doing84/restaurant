from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model): 
    # 이름 
    name = models.CharField(max_length=50) 
    # 카테고리 (ForeignKey로 변경)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    # 주소 
    address = models.CharField(max_length=255) 
    # 전화번호 
    phone = models.CharField(max_length=20) 
    # 위도 
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 경도 
    longitude = models.DecimalField(max_digits=9, decimal_places=6) 
    # 점수 
    rating = models.SmallIntegerField() 
    # 생성 시간 
    created_at = models.DateTimeField(auto_now_add=True) 
    # 업데이트 시간 
    updated_at = models.DateTimeField(auto_now=True)
    # 방문자수
    visitor_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name