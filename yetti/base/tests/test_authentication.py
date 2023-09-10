from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = User.objects.create_user(**self.user_data)
        
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',  # Confirm password
        })

        # Check for a 200 status code (indicating a successful registration with validation errors)
        self.assertEqual(response.status_code, 200)

        # Check if the user is logged in (if registration is successful, it should auto-login)
        user = self.client.session.get('_auth_user_id')
        



    def test_login(self):
        response = self.client.post(reverse('login'), self.user_data)
        self.assertEqual(response.status_code, 302)  # 302 indicates a successful redirect after login
        user = self.client.session.get('_auth_user_id')
        self.assertTrue(user)

    def test_logout(self):
        login_response = self.client.post(reverse('login'), self.user_data)
        self.assertEqual(login_response.status_code, 302)  # 302 indicates a successful redirect after login
        logout_response = self.client.get(reverse('logout'))
        self.assertEqual(logout_response.status_code, 302)  # 302 indicates a successful redirect after logout
        user = self.client.session.get('_auth_user_id')
        self.assertIsNone(user)  # User should be logged out
