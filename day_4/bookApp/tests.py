from django.test import TestCase
from .models import Category, Book, Author

# Create your tests here.
class CategoryModelTest(TestCase):
    """
    test
    """
    def setUp(self):
        """
        Set up non-modified objects used by all test methos.
        """
        Category.objects.create(name='test',description='test',status=True)
    
        
    
    def test_category_name_is_not_blank(self):
        """test for category name is no blank
        """
        category = Category.objects.get(id=1)
        self.assertIsNot(category.name, '')

    
        
    

