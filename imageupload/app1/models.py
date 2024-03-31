from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads')
    # image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'users'
