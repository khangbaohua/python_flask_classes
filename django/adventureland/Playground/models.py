from django.db import models

class Toy(models.Model):
    name=models.CharField(max_length=50)
    age_recommended=models.IntegerField()

    def __str__ (self):
        return self.name
# Create your models here.
