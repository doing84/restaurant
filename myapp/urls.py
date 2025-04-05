from django.urls import path
from . import views
from .views import PersonListAPIView, PersonDetailAPIView
from .views import TestListAPIView, TestDetailAPIView

urlpatterns = [
    path('people/', views.show_people, name='people'),
    path('api/people/', PersonListAPIView.as_view(), name='api-people'),
    path('api/people-func/', views.person_list_function, name='api-people-func'),
    path('api/people/<int:pk>/', PersonDetailAPIView.as_view(), name='api-people-update'),
    path('api/people-sql-update/<int:person_id>/', views.PersonSQLUpdateAPIView.as_view(), name='people-sql-update'),
    path('api/people-sql-detail/<int:person_id>/', views.PersonSQLDetailAPIView.as_view(), name='people-sql-detail'),
    path('api/test/', TestListAPIView.as_view(), name='api-test'),
    path('api/test/<int:pk>/', TestDetailAPIView.as_view(), name='api-test-detail'),
    
]
