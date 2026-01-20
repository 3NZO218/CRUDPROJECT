from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, Author, Publisher

class BookTests(TestCase):
    def setUp(self):
        self.user_a = get_user_model().objects.create_user(
            username='user_a', password='password123'
        )
        self.user_b = get_user_model().objects.create_user(
            username='user_b', password='password123'
        )
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.book = Book.objects.create(
            title='Test Book',
            user=self.user_a,
            body='Test Body',
            price=10.00,
            rating=5,
            pub_date='2023-01-01',
            publisher=self.publisher
        )

    def test_book_create_view(self):
        self.client.login(username='user_a', password='password123')
        response = self.client.post(reverse('book_create'), {
            'title': 'New Book',
            'body': 'New Body',
            'price': 20.00,
            'rating': 4,
            'pub_date': '2023-01-02',
            'publisher': self.publisher.id,
        })
        # Assuming successful creation redirects; check status 302
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title='New Book').exists())
        self.assertEqual(Book.objects.get(title='New Book').user, self.user_a)

    def test_book_update_view_owner(self):
        self.client.login(username='user_a', password='password123')
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'title': 'Updated Title',
            'body': 'Test Body',
            'price': 10.00,
            'rating': 5,
            'pub_date': '2023-01-01',
            'publisher': self.publisher.id,
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_book_update_view_non_owner(self):
        self.client.login(username='user_b', password='password123')
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'title': 'Hacked Title',
            'body': 'Test Body',
            'price': 10.00,
            'rating': 5,
            'pub_date': '2023-01-01',
            'publisher': self.publisher.id,
        })
        self.assertEqual(response.status_code, 403)
        self.book.refresh_from_db()
        self.assertNotEqual(self.book.title, 'Hacked Title')

    def test_book_delete_view_owner(self):
        self.client.login(username='user_a', password='password123')
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_book_delete_view_non_owner(self):
        self.client.login(username='user_b', password='password123')
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Book.objects.filter(id=self.book.id).exists())
