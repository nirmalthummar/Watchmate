from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            username="user1",
            password="Kaushik@123"
        )

    def test_stream_platform_create(self):

        data = {
            "name": "MX Player",
            "about": "This is new platform",
            "website": "https://www.mxplayer.com"
        }
        response = self.client.post(reverse('stream-platform-model-view-set'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
