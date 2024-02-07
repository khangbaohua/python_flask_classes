from django.db import models
class Item(models.Model):
    title=models.CharField(max_length=50)
    completed=models.BooleanField()
    
    def __str__ (self):
        return self.title




# Create your models here.
