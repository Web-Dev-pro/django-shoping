from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'Mominjon',
                'username':'mominjon',
                'email':'mominjon@gmail.com',
                'password1':'mominjon',
                'password2':'mominjon',
            }
        )
        user = CustomUser.objects.get(username='mominjon')
        self.assertEqual(user.first_name, 'Mominjon')
        self.assertEqual(user.email, 'mominjon@gmail.com')
        self.assertTrue(user.check_password, 'mominjon')


        # second_response = self.client.get('/users/profile/django')
        # self.assertEqual(second_response.status_code, 200)