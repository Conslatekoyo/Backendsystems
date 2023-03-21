from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="question")
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="answer")
    questions=models.ForeignKey(Questions,on_delete=models.SET_NULL,null=True,related_name="answer")
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.content
        

