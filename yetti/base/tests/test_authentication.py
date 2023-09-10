from django.test import TestCase 
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        return super().setUp()
    

class RegisterTest(BaseTest):
    def test_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'registration/register.html')