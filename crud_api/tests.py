from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase 
from crud.models import User

# Create your tests here.
class PostTests(APITestCase):
    
    def test_view_posts(self):
        
        url = reverse('crud_api:listuser')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
