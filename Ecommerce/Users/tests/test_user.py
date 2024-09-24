from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group

class UserAuthTests(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')  # URL for registering a user
        self.login_url = reverse('login')        # URL for logging in
        self.logout_url = reverse('logout')      # URL for logging out

        # Create the user groups (buyers and sellers)
        Group.objects.get_or_create(name='buyers')
        Group.objects.get_or_create(name='sellers')

        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123',
            'group': 'buyers'  # The user will join the 'buyers' group during registration
        }

    def test_user_registration_with_group(self):
        """ Test user registration and group assignment """
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)  # Ensure token is included in the response

        user = User.objects.get(username='testuser')
        buyers_group = Group.objects.get(name='buyers')
        
        # Check that the user was added to the 'buyers' group
        self.assertIn(buyers_group, user.groups.all())

    def test_user_login(self):
        """ Test that a registered user can log in successfully """
        # First, create a user directly in the test database
        User.objects.create_user(username='testuser', password='testpassword123')

        # Now, attempt to log in with the created user's credentials
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(self.login_url, login_data, format='json')

        # Ensure the response is successful and contains the authentication token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_user_logout(self):
        """ Test that a logged-in user can log out successfully """
        # First, create a user and log them in
        User.objects.create_user(username='testuser', password='testpassword123')
        
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        
        # Get the token from the login response
        token = login_response.data['token']

        # Set the Authorization header with the Bearer token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        # Now attempt to log out
        logout_response = self.client.post(self.logout_url)

        # Check that the logout was successful
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)

