 BIN +1.04 KB (140%) TechReviewProject/TechReviewApp/__pycache__/tests.cpython-36.pyc 
Binary file not shown.
  27  TechReviewProject/TechReviewApp/tests.py 
@@ -2,6 +2,8 @@
from django.urls import reverse
from .models import TechType, Product, Review
from django.contrib.auth.models import User
import datetime
from .forms import ProductForm

# Create your tests here.clear
#test for models
@@ -44,3 +46,28 @@ def test_product_detail_success(self):
        response=self.client.get(reverse('productdetail', args=(self.prod.id,)))
        self.assertEqual(response.status_code, 200)

class ProductFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type2=TechType.objects.create(techtypename='type1')

    def test_productForm(self):
        data={
            'productname' : 'product1',
            'techtype' : self.type2,
            'user' : self.user2,
            'productprice' : 200.00,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid)

    def test_productFormInvalid(self):
        data={
            'productname' : 'product1',
            'techtype' : 'type1',
            'user' : self.user2,
            'productentrydate' : datetime.date(2019,5,28),
        }
        form = ProductForm(data=data)
        self.assertFalse(form.is_valid()) 
