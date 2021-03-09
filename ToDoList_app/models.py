from django.db import models

# Create your models here.
class Activity(models.Model):
    name=models.CharField(null=True,max_length=50)
    def __str__(self):
        return self.name