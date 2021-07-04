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

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    # Test saving images
    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    # test delete images
    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)