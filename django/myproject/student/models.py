from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    student_id=models.IntegerField()
    grade=models.CharField(max_length=2)
    lunch_money=models.IntegerField()
    
    def __str__(self):
        return self.student_id
# Create your models here.
