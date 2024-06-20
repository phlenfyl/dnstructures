from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class SignupViewTest(TestCase):
    def test_user_signup(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/auth/register/', data)
        self.assertEqual(response.status_code, 200)
        user = get_user_model().objects.get(email='test@example.com')
        self.assertNotEqual(user.password, 'testpassword')  # Ensure the password is not stored in plain text
        self.assertTrue(user.check_password('testpassword'))  #
