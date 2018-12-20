from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
    """
    We will define the tests
    we'll run against product models
    """
    
    def test_str(self):
        test_name = Product(name='a product')
        self.assertEqual(str(test_name), 'a product')
        
