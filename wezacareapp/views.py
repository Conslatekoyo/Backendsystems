from django.shortcuts import render
from rest_framework import authentication,generics,permissions
from .models import *
from .serializers import *

# Create your views here.

class QuestionListAPIView(generics.ListAPIView):
    queryset=Questions.objects.all()
    serializer_class=QuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class=QuestionSerializer
    permission_classes=(permissions.IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    def create(self,serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset=Questions.objects.all()
    serializer_class=QuestionSerializer


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset=Questions.objects.all()
    serializer_class=QuestionSerializer
    #TODO:permission classes

    #def get_queryset(self):
        #return super().get_queryset().filter(author=self.request.user)
    

class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset=Questions.objects.all()
    serializer_class=QuestionSerializer
    #TODO:permission classes

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AnswerListAPIView(generics.ListAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class=AnswerSerializer

    def create_answer(self,serializer):
        serializer.save(author=self.request.user)

class AnswerRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class=AnswerSerializer
    #TODO:permission classes

class AnswerDeleteAPIView(generics.DestroyAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
    
class AnswerUpdateAPIView(generics.UpdateAPIView):
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer

    def get_queryset(self):
        return super().get_queryset()
    

    

   



