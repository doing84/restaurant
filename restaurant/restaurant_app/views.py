from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("레스토랑 앱에 오신 걸 환영합니다!")