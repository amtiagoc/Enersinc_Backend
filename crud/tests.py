from django.test import TestCase
from crud.models import User

# Create your tests here.
class UserTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(tipo_doc='CC', doc='123456789', name='John', surnames='Doe', hobbie='1')
        
    
    def test_user_detail(self):
        user = User.objects.get(id=1)
        hob = f'{user.hobbie}'
        name = f'{user.name}'
        surnames = f'{user.surnames}'
        tipo_doc = f'{user.tipo_doc}'
        self.assertEqual(name, 'John')
        self.assertEqual(surnames, 'Doe')
        self.assertEqual(tipo_doc, 'CC')
        self.assertEqual(hob, '1')
        self.assertEqual(str(user), 'John')
        
      
