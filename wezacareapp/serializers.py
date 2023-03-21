from .models import *
from rest_framework import serializers



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields="__all__"
        extra_kwargs = {
            "author": {"read_only": True}
       }
        

class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=["text"]

class QuestionSerializer(serializers.ModelSerializer):
    answers=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Questions
        fields="__all__"
    def get_answers(self, obj):
        answers = obj.answer
        serializers = AnswerSerializer(answers, many=True)
        return serializers.data    
    
        
