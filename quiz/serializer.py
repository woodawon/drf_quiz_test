from rest_framework import serializers
from .models import Quiz

# serializer(시리얼라이저) : 
# 장고 모델 데이터를 JSON 타입으로 바꿔주는(직렬화) 코드

# 장고 모델 데이터를 템플릿에 뿌려주면 웹에 보여지듯,
# JSON 타입으로 뿌려주면 api로 통신이 되는 것이며
# 내 데이터를 JSON으로 바꿔주는 기계라고 이해하면 됨

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')