from django.db import models

# Create your models here.

class Feed(models.Model):
    title= models.CharField(max_length=20)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
