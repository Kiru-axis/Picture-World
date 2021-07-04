from django.test import TestCase
from .models import Image, Category, Location
# Create your tests here.
class TestImage(TestCase):
    # setup method to inherit from
    def setUp(self):
        self.location = Location(name='Location')
        self.location.save_location()

        self.category = Category(name='food')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='test image', location=self.location,category=self.category)
    # Tear down after each test
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()