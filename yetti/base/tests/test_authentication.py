from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user

class BaseTest(TestCase):
    def setUp(self) -> None:
        self.user = {
            'username':'userone',
            'email':'test@example.com',
            'password1':'password',
            'password2':'password'
        },
        self.user2 = {
            'username':'user',
            'email':'test@example.com',
            'password1':'test',
            'password2':'test'
        }
        self.register_url = reverse('register')
        return super().setUp()
    

class RegisterTest(BaseTest):
    def test_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'registration/register.html')

    # def test_can_register_user(self):
    #     response = self.client.post(self.register_url, self.user, format="text/html")
    #     self.assertEqual(response.status_code, 200)

    # def test_cant_register_with_short_password(self):
    #     response = self.client.post(self.register_url, self.user2, format="text/html")
    #     self.assertEqual(response.status_code, 200)

class LoginTest(BaseTest):
    def test_login(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(username = 'Yego', password = 'another12')
        self.assertTrue(get_user(self.client).is_authenticated)