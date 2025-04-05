from django.contrib import admin
from .models import Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    #목록 뷰에 표시될 필드
    list_display = [
        'id', 
        'name', 
        'phone', 
        'rating',
        'visitor_count',
        'created_at',
        'updated_at',
    ]
    # 상세 뷰에 표시될 필드
    fields = ['name', 'phone', 'rating', 'latitude', 'longitude', 'visitor_count']


admin.site.register(Restaurant, RestaurantAdmin)