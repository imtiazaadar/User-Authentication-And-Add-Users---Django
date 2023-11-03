from django.db import models
# Name : Imtiaz Adar
# Project : User Authentication And Adding Users
# Language : Python
# Framework : Django
# Phone : 01778767775, 01979777379
# Email : imtiazadarofficial@gmail.com
# Create your models here.
class Information(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.IntegerField()
    current_location = models.CharField(max_length=100)
    hometown_location = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    
    def __str__(self):
        return self.fullname
    
    