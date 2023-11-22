from django.db import models

# models.py 에서 새로운 모델을 만들거나 수정했을 때

# 새로운 모델을 생성 or 수정 시 DB 스키마를 변경하는 마이그레이션 파일 생성 (일종의 로그)
# $ python3 manage.py makemigrations

# 마이그레이션 파일을 기반으로 DB 스키마를 실제 DB 에 업데이트
# $ python3 manage.py migrate

class kimDB(models.Model):
    # 모델 객체의 고유 식별자 'id' 는 django에서
    # 자동으로 생성되서 따로 설정할 필요가 없다!
    text_fields = models.TextField(max_length=200)
    bool_fields = models.BooleanField()
    char_fields = models.CharField(max_length=40)
    
    # kimDB 객체(즉, DB에 저장된 kimDB) 를 조회 했을 때 반환(보여질)할 값 들을 설정한다.
    # 즉, 해당 모델의 인스턴스가 문자열로 표현될 때 어떤 정보를 보여줄지를 지정
    # 그리고, 반환 값은 튜플 말고 문자열로 하자!
    def __str__(self):
        return f'text_fields : {self.text_fields}, bool_fields : {self.bool_fields}, char_fields : {self.char_fields}'