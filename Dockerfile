# Python 3.11을 기반으로 설정
FROM python:3.11

# 작업할 디렉토리 설정
WORKDIR /app

# 로컬의 requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt /app/

# requirements.txt에 있는 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일들을 컨테이너로 복사
COPY . /app/

# Django 서버 실행
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
