from django.db import models
# Create your models here.
class Patient(models.Model):
    fist_name       = models.CharField(max_length=50)
    lastname_name   = models.CharField(max_length=50)
    phone           = models.CharField(max_length=30) 
    date_of_birth   = models.DateField(auto_now=False, auto_now_add=False)
    registered      = models.DateTimeField(auto_now_add=True)
    email           = models.EmailField()
    avatar          = models.ImageField()

class Comments(models.Model):
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    date        = models.DateTimeField(auto_now_add=True)