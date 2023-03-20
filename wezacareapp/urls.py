from django.urls import path
from . import views


urlpatterns=[
    path("",views.QuestionListAPIView.as_view(),name="questions_list"),
    path("create/",views.QuestionCreateAPIView.as_view(),name="questions_create"),
    path("retrieve/<int:pk>/",views.QuestionRetrieveAPIView.as_view(),name="questions_retrieve"),
    path("delete/<int:pk>/",views.QuestionDeleteAPIView.as_view(),name="questions_delete"),
    path("update/<int:pk>/",views.QuestionUpdateAPIView.as_view(),name="questions_update"),
    path("answers/",views.AnswerListAPIView.as_view(), name="answer_list"),
    path("answercreate/",views.AnswerCreateAPIView.as_view(),name="answer_create"),
    path("answerretrieve/",views.AnswerRetrieveAPIView.as_view(),name="answer_retrieve"),
    path("answerdelete/<int:pk>",views.AnswerDeleteAPIView.as_view(),name="answer_delete"),
    path("answerupdate/<int:pk>",views.AnswerUpdateAPIView.as_view(),name="answer_update"),

    

]
