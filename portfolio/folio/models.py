from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MyInfo(models.Model):
    image = CloudinaryField('image', null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    

    def __str__(self):
        return self.title
