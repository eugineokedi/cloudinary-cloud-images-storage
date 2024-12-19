from django.db import models
from cloudinary.models import  CloudinaryField

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('image')
