from django.db import models

# Create your models here.
class QuizHeading(models.Model):
    name=models.TextField(null=True)

    def __str__(self):
        return  f'{str(self.name)} {self.id}'

class MCQ_Gen(models.Model):
    name=models.ForeignKey(QuizHeading,on_delete=models.CASCADE),
    code=models.IntegerField(null=True)
    que=models.TextField(null=True)
    ans=models.TextField(null=True)
    opt1=models.TextField(null=True)
    opt2=models.TextField(null=True)
    opt3=models.TextField(null=True)
    opt4=models.TextField(null=True)
