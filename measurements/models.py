from django.db import models

# Create your models here.
class Ranges(models.Model):
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=0)
    min_normal_pulse = models.IntegerField(default=0)
    max_normal_pulse = models.IntegerField(default=0)
    min_limit = models.IntegerField(default=0)
    max_limit = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, blank=True)