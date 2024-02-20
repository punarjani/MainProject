from django.db import models

# Create your models here.
class Adduser(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    contactno=models.CharField(max_length=100)

class Addpatient(models.Model):
    prevhist=models.CharField(max_length=100)
    curcond=models.CharField(max_length=100)
    name=models.CharField(max_length=100)  
    age=models.CharField(max_length=100)  
    sex=models.CharField(max_length=100)  
    bystandname=models.CharField(max_length=100)  
    contactno=models.CharField(max_length=100) 
     
class actiontaken(models.Model):
    fanon=models.CharField(max_length=100)  
    fanoff=models.CharField(max_length=100)  
    lighton=models.CharField(max_length=100)  
    lightoff=models.CharField(max_length=100)  
    acon=models.CharField(max_length=100)  
    acoff=models.CharField(max_length=100)  
    emergencyalarm=models.CharField(max_length=100)  
    bedorientation=models.CharField(max_length=100)  


