# admin 페이지와 새로 생성된 모델간의 연결

from django.contrib import admin
# models.py 에서 정의한 UserDB를 가져오기
from .models import UserDB

# UserDB 연동
admin.site.register(UserDB)