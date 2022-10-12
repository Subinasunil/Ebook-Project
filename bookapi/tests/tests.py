from django.test import TestCase
from rest_framework.reverse import reverse
from bookapi.models import Books
from rest_framework.test import APITestCase
from rest_framework import  status

class BookTestCase(APITestCase):

    def test_book(self):
        book_data = {
            'title': 'shiva',
            'author': 'priya',
            'genre': 'mystery',
            'favourite': False
        }
        book_obj = Books.objects.create(**book_data)
        url = reverse('book')
        response = self.client.post(url, {'pk': book_obj.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
