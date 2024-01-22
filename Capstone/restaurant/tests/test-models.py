from django.test import TestCase
from restaraunt.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from restaraunt.serializers import MenuSerializer
from rest_framework import status

class MenuTest(TestCase):
    def test_add_menu_insance(self):
        menu_item = Menu.objects.create(name='New Dish', price=12.99)
        anticipated_value = f"{menu_item.name} - ${menu_item.price}"
        self.assertEqual(str(menu_item), anticipated_value)

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name='Dish 1', price=10.99)
        Menu.objects.create(name='Dish 2', price=15.99)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu')  # Assuming you have a 'menu-list' endpoint in your urls
        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        menu_objects = Menu.objects.all()
        serializer = MenuSerializer(menu_objects, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
# Create your tests here.
