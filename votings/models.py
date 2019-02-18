from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Published date')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    chioce_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
