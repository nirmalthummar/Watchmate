from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):

        data = {
            "username": "kaushik",
            "email": "kaushik@gmail.com",
            "password": "kaushik@123",
            "password2": "kaushik@123"
        }

        response = self.client.post(reverse('registration_view'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="user1",
            password="Kaushik@123"
        )
        self.token = Token.objects.get(user__username="user1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_login(self):
        data = {
            "username": "user1",
            "password": "Kaushik@123"
        }
        response = self.client.post(reverse('login'), data)
        print("response is...", response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="user1")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
