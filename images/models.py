from django.db import models
from cloudinary.models import  CloudinaryField
import cloudinary.uploader

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('image')
    
    def save(self, *args, **kwargs):
        # Check if the image is updated or new
        if self.image and hasattr(self.image, 'file'):
            # Upload the image to a specific folder
            upload_result = cloudinary.uploader.upload(
                self.image.file,
                folder="Cloudinary_cloud_storage"
            )
            # Save only the public ID for storage efficiency
            self.image = upload_result["public_id"]
        
        super().save(*args, **kwargs)
