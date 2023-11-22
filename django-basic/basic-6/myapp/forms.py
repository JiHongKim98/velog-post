from django import forms
# 우리가 생성한 모델 import
from .models import kimDB

class htmlForm(forms.ModelForm):

    # Meta class는 models.py 와 forms.py 를 연동 시켜주는 역활을 해준다.
    class Meta:
        # kimDB 라는 모델과 연동 되어있다.
        model = kimDB

        # fields 는 html 파일 폼에서 사용할 model의 fields 목록을 지정해준다.
        fields = ['text_fields', 'bool_fields', 'char_fields']

        # Meta class 는 model, fields 이외에
        # widgets : 폼 필드의 입력 방식 지정. ex, 텍스트 필드에 forms.TextInput 등을 사용하여 사용자 정의 위젯을 설정
        # labels : 폼 필드의 화면에 표시되는 레이블(텍스트)을 사용자 정의
        # help_texts : 폼 필드에 대한 도움말 텍스트를 설정
        # error_messages : 폼 필드에서 발생하는 유효성 검사 오류에 대한 사용자 지정 오류 메시지를 설정
        # ordering : 모델에서 가져온 데이터의 정렬 순서를 설정
        # exclude : 특정 필드를 폼에서 제외
        # localized_fields : 지역화된 필드(예: 날짜 및 시간)의 형식을 지정
        # field_classes : 특정 필드에 사용자 정의 폼 필드 클래스를 할당
        # 등이 있다!