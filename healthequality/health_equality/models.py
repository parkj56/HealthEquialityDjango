from django.db import models

# Create your models here.
class BodyData(models.Model):
    age = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    dose = models.CharField(max_length=50)
    start_date = models.DateField()
    dose_date = models.DateField()
