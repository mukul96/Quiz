from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer=models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    ch1=models.TextField(max_length=100)
    ch2=models.TextField(max_length=100)
    ch3=models.TextField(max_length=100)
    ch4=models.TextField(max_length=100)

  
class Stan(models.Model):
	 ques=models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
         reponse=models.CharField(max_length=200 ,default='0000000')
