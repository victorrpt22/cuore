from django.db import models
# Create your models here.
class Patient(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone           = models.CharField(max_length=30) 
    date_of_birth   = models.DateField(auto_now=False, auto_now_add=False)
    registered      = models.DateTimeField(auto_now_add=True)
    email           = models.EmailField(blank=True)
    avatar          = models.ImageField(blank=True, upload_to='patient/uploaded_images/')
    status          = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.email + ")" 

class Comments(models.Model):
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    date        = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description

class notification(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)