from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/')