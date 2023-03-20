from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Questions
        fields="__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields="__all__"

class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=["text"]
        
