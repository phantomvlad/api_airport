from django.urls import reverse, path
from rest_framework import status
from rest_framework.test import APITestCase , URLPatternsTestCase
from .models import Aircraft

class AccountTests(APITestCase, URLPatternsTestCase):
    def test_create_aircraft(self):
        url = reverse('api:aircrafts-aircrafts-create')
        data = {'icao_code': 'T123', 'iata_code': 'T12', 'aircraft_name': 'testName', 'extra_info': ''}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Aircraft.objects.count(), 1)
        self.assertEqual(Aircraft.objects.get().aircraft_name, 'testName')