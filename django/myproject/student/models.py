from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    student_id=models.IntegerField()
    grade=models.CharField(max_length=2)
    lunch_money=models.IntegerField()
    
    def __str__(self):
        return self.student_id
    
class Banana(models.Model):
    color=models.CharField(max_length=50)
    size=models.IntegerField()
    def __str__(self):
        return self.color
# Create your models here.
