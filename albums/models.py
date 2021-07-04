from django.db import models
from django.utils import timezone
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Image(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=40, default='admin')
    description = models.TextField()
    date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    location = models.ForeignKey(Location,on_delete= models.CASCADE)
# on_delete= models.CASCADE : Telling django to delete the post once the author is deleted
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    # update images
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

