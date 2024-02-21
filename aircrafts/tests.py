from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Aircraft
from .serializers import AircraftSerializer


class AircraftTests(APITestCase):
    def setUp(self):
        self.aircraft_data = {'icao_code': 'T123', 'iata_code': 'T12', 'aircraft_name': 'testName', 'extra_info': ''}
        self.aircraft = Aircraft.objects.create(**self.aircraft_data)

    def test_list_aircrafts(self):
        response = self.client.get(reverse('aircrafts-list')+'?offset=0&limit=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_aircrafts(self):
        url = reverse('aircrafts-list')
        serializer = AircraftSerializer(data=self.aircraft_data)  # Создание экземпляра сериализатора с data
        self.assertTrue(serializer.is_valid())  # Проверка валидности данных
        response = self.client.post(url, data=self.aircraft_data, format='json')  # Передача данных для создания объекта
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Aircraft.objects.count(), 2)  # Проверка количества объектов в базе данных
        self.assertEqual(Aircraft.objects.last().aircraft_name,
                         'testName')  # Проверка имени последнего созданного объекта

