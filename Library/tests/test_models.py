from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from Library.models import Author, Book
from model_bakery import baker


class BaseModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = baker.make(Author)
        cls.book = baker.make(Book, author=cls.author)


class AuthorModelTest(BaseModelTestCase):

    def test_author_creation(self):
        self.assertTrue(isinstance(self.author, Author))
        self.assertEqual(str(self.author), f'{self.author.surname} {self.author.name}')

    def test_name_is_alpha_validator(self):
        self.author.name = '1222'
        with self.assertRaises(ValidationError):
            self.author.full_clean()

    def test_surname_is_alpha_validator(self):
        self.author.surname = '1222'
        with self.assertRaises(ValidationError):
            self.author.full_clean()

    def test_get_absolute_url(self):
        response = self.client.get(reverse('author_detail', kwargs={'author_id': self.author.author_id}))
        self.assertEqual(response.status_code, 200)


class BookModelTest(BaseModelTestCase):
    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(str(self.book), f'{self.book.title} - {self.author}')

    def test_year_validator(self):
        self.book.year = 2042
        with self.assertRaises(ValidationError):
            self.book.full_clean()

    def test_correct_author(self):
        self.assertEqual(self.author, self.book.author)

    def test_get_absolute_url(self):
        response = self.client.get(reverse('book_detail', kwargs={'book_id': self.book.book_id}))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    author_model_test = AuthorModelTest()
    book_model_test = BookModelTest()
