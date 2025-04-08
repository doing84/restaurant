from django.contrib import admin
from .models import Restaurant, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    # 목록 뷰에 표시될 필드
    list_display = [
        'id', 
        'name',
        'category', 
        'phone', 
        'rating',
        'visitor_count',
        'created_at',
        'updated_at',
    ]
    # 상세 뷰에 표시될 필드
    fields = [
        'name', 
        'category', 
        'address',  
        'phone', 
        'rating',
        'latitude', 
        'longitude', 
        'visitor_count'
    ]

    list_filter = ['category', 'rating']
    search_fields = ['name', 'category', 'address', 'phone']

    actions = ['reset_ratings', 'set_5_ratings']  

    @admin.action(description="선택된 가게의 별점을 초기화")
    def reset_ratings(self, request, queryset):
        """선택된 레스토랑의 평점을 0으로 초기화"""
        updated_count = queryset.update(rating=0)
        self.message_user(request, f"{updated_count}개의 레스토랑의 별점이 초기화되었습니다.")
    
    @admin.action(description="선택된 가게의 별점을 5로 설정")
    def set_5_ratings(self, request, queryset):
        """선택된 레스토랑의 평점을 5로 설정"""
        updated_count = queryset.update(rating=5)
        self.message_user(request, f"{updated_count}개의 레스토랑의 별점이 5로 설정되었습니다.")