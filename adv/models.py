from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class content:
    htag:str
    para:str
    img:str

class Electronics:
    img:str
    title:str
    desc:str
    offer:bool

class MyClass(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='img',null=True)
    desc = models.TextField()
    no = models.IntegerField()
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    empid = models.IntegerField(max_length=20)
    address = models.TextField(max_length=400)
    mobile = models.IntegerField(max_length=10)
    position = models.CharField(max_length=20)
    