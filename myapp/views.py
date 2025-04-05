from django.shortcuts import render
from django.http import HttpResponse
from .models.test_model import Test
from .models.person import Person
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .serializers import TestSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db import connection

# 새로운 REST API 뷰 (JSON 응답)
class PersonListAPIView(APIView):
    def get(self, request):
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

class PersonDetailAPIView(APIView):
    def put(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersonSQLUpdateAPIView(APIView):
    def put(self, request, person_id):
        name = request.data.get('name')
        age = request.data.get('age')

        if not name or not age:
            return Response({'error': 'name과 age는 필수입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # SQL 쿼리 직접 작성
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE myapp_person SET name = %s, age = %s WHERE id = %s",
                [name, age, person_id]
            )
        return Response({'message': '성공적으로 수정되었습니다.'}, status=status.HTTP_200_OK)
        
class PersonSQLDetailAPIView(APIView):
    def get(self, request, person_id):
        # SQL 쿼리 직접 작성하여 수정된 데이터 가져오기
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, age FROM myapp_person WHERE id = %s", [person_id]
            )
            row = cursor.fetchone()

        if row:
            # 반환된 결과를 JSON으로 변환하여 Response로 반환
            person = {'id': row[0], 'name': row[1], 'age': row[2]}
            return Response(person, status=status.HTTP_200_OK)
        return Response({'error': '사람을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

def show_people(request):
    people = Person.objects.all()
    names = ', '.join([f'{p.name} ({p.age})' for p in people])
    return HttpResponse(f"사람들 목록: {names}")

@api_view(['GET', 'POST'])
def person_list_function(request):  # ← 이름 구분!
    if request.method == 'GET':
        people = Person.objects.all()
        data = [{'name': p.name, 'age': p.age} for p in people]
        return Response(data)

    elif request.method == 'POST':
        name = request.data.get('name')
        age = request.data.get('age')

        if not name or not age:
            return Response({'error': 'name과 age는 필수입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        person = Person.objects.create(name=name, age=age)
        return Response({'message': '생성 완료!', 'id': person.id}, status=status.HTTP_201_CREATED)
    
class TestListCreateAPIView(APIView):
    def get(self, request):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)