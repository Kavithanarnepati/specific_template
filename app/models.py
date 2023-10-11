from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)


    def __str__(self):
        return self.Sname
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})



class Student(models.Model):
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.stname