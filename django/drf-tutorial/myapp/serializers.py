from rest_framework import serializers
from myapp.models import testdb

class testdbSerializer(serializers.ModelSerializer):

    class Meta:
        # ModelSerializer 를 활용할 모델
        model = testdb
        # 데이터를 전부 사용하고 싶다면
        # '__all__' 을 통해 모든 데이터를 사용 가능
        fields = ['id', 'charFields1', 'charFields2', 'content']