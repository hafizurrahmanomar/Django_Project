from django.db import models

# Create your models here.

class MyBlogPost(models.Model):
    title=models.CharField(max_length=300,blank=True,null=True)
    author=models.CharField(max_length=250,default="")
    body=models.TextField()
   

    