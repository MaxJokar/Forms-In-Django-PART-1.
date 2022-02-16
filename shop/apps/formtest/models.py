from cProfile import label
from django.db import models
from django.utils import timezone

class Person(models.Model):
    name=models.CharField(max_length=20)
    
class Post(models.Model):
    title=models.CharField(max_length=50,verbose_name="Title of Post")
    description=models.TextField(max_length=300,verbose_name="Description")
    is_active=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title+" "+self.description+" "+str(self.is_active)

#our Model is created
# class Author(models.Model):
    # id=models.IntegerField(primary_key=True)
    # name=models.CharField(max_length=30)
    # family=models.CharField(max_length=30)
    # slug=models.SlugField(max_length=100)
    # age=models.IntegerField(default=20)
    # is_active=models.BooleanField(default=True)
    # register_date=models.DateTimeField(default=timezone.now)
    # email=models.EmailField(max_length=100)
    # image_name=models.CharField(max_length=200,default='nophoto',null=True,blank='True')
    
    
    # def __str__(self) :
    #     return f"{self.name}\t{self.family}\t{self.age}"