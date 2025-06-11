from django.urls import reverse
from django.test import TestCase
from django.http import HttpResponse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.item1 = Menu.objects.create(
        Title='IceCream', Price=2.95, Inventory=100)
    self.item2 = Menu.objects.create(Title='Pizza', Price=5.95, Inventory=24)
    self.item3 = Menu.objects.create(Title='Burger', Price=7.99, Inventory=55)

  def test_getall(self):
    response: HttpResponse = self.client.get(reverse('menu-view'))
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
