from django.db import models
from django.utils import timezone
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod #applicable to the entire class. Not limited to the defined function
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=50)

    # output format
    def __str__(self):
        return self.name

    # save category
    def save_category(self):
        self.save()
    # delete category
    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=60)
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

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
    
    # save image
    def save_image(self):
        self.save()
        
     # delete image
    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']


    def __str__(self):
        return self.name
