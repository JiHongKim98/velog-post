from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 장고 모델과 ModelSerializer
from .models import testdb
from .serializers import testdbSerializer

# HTTP Method 지정 데코레이터
# api_view 데코를 사용해서 장고의 view 함수가
# API view 함수로 동작하도록 해준다.
@api_view(['GET', 'POST'])
def myAPI(request):
    if request.method == 'GET':
        test = testdb.objects.all()
        # many=True 는 여러 모델 처리 허용 관련된 옵션
        serializer = testdbSerializer(test, many=True)

        # state 옵션을 사용해서 HTTP 상태 코드를 보여준다.
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = testdbSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() # 역직렬화
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)