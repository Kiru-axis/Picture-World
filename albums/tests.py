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

    # update images
    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)
    
    # search images by id
    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    # search images by location
    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Location')
        self.assertTrue(len(found_images) == 1)
    
    # search images by category
    def test_search_image_by_category(self):
        category = 'food'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)
