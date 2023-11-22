from django.db import models
from django.contrib.auth.models import AbstractUser

# 'UserDB' 라는 새로운 모델에 장고 기본 User 모델을 상속받았다.
class UserDB(AbstractUser):
	# add room_name fields
	room_name = models.CharField(max_length=50)
    
# 생성후 마이그레이션 적용 잊지 말자!
# 마이그레이션 적용법은 '모델과 폼' 게시글에서 볼 수 있다.