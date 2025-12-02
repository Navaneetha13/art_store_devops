from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
from art_store import views   

class URLTests(TestCase):

    def test_index_page_loads(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
        
    def test_view_artproduct_invalid_id(self):
        response = self.client.get('/ViewArtProduct/9999')
        self.assertEqual(response.status_code, 302)

        
    
    def test_login_without_credentials(self):
        response = self.client.post(reverse('doLogin'), {})
        self.assertIn(response.status_code, [200, 302])

