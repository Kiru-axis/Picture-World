from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=60)
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    location = models.ForeignKey(Location,on_delete= models.CASCADE)
# on_delete= models.CASCADE : Telling django to delete the post once the author is deleted

