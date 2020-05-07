from django.forms import model_to_dict
from django.test import TestCase, RequestFactory

from Library.views import *
from model_bakery import baker


class BaseViewTestCaseMixin(object):

    @classmethod
    def setUpTestData(cls):
        cls.view = None  # Check the correct view
        cls.url = None  # Check if url is correct
        cls.url_name = None  # Check the verbose url name
        cls.template_name = None
        cls.context = None # For views with context argument

    def test_status_code(self):
        response = self.client.get(self.url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_correct_url(self):
        response = self.client.get(reverse(self.url_name, kwargs=self.context))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse(self.url_name, kwargs=self.context))
        self.assertTemplateUsed(response, self.template_name)


class IndexViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = IndexPageView
        cls.url = '/library/'
        cls.url_name = 'index'
        cls.template_name = 'index.html'
        cls.context = None


class SearchTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = SearchResultView
        cls.url = '/library/search/'
        cls.url_name = 'search_results'
        cls.template_name = 'search_results.html'
        cls.context = None
        cls.factory = RequestFactory()
        cls.book = baker.make(Book)
        cls.author = baker.make(Author)


class AuthorListViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = AuthorListView
        cls.url = '/library/authors/'
        cls.url_name = 'authors'
        cls.template_name = 'authors.html'
        cls.context = None


class BookListViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = BookListView
        cls.url = '/library/books/'
        cls.url_name = 'books'
        cls.template_name = 'books.html'
        cls.context = None


class AuthorDetailViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = AuthorDetailView
        cls.author = baker.make(Author)
        cls.url = f'/library/authors/{cls.author.author_id}/'
        cls.url_name = 'author_detail'
        cls.template_name = 'author_detail.html'
        cls.context = {'author_id': cls.author.author_id}


class BookDetailViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = BookDetailView
        cls.book = baker.make(Book)
        cls.url = f'/library/books/{cls.book.book_id}/'
        cls.url_name = 'book_detail'
        cls.template_name = 'book_detail.html'
        cls.context = {'book_id': cls.book.book_id}


class BookCreateViewTestCase(TestCase, BaseViewTestCaseMixin):
    @classmethod
    def setUpTestData(cls):
        cls.view = BookCreateView
        cls.author = baker.make(Author)
        cls.book = baker.make(Book)
        cls.url = f'/library/books/create'
        cls.url_name = 'book_create'
        cls.template_name = 'book_create.html'
        cls.context = None

    def test_post_request(self):
        response = self.client.post(self.url, model_to_dict(self.book))
        self.assertEqual(response.status_code, 200)


class AuthorCreateViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = AuthorCreateView
        cls.author = baker.make(Author)
        cls.url = f'/library/authors/create'
        cls.url_name = 'author_create'
        cls.template_name = 'author_create.html'
        cls.context = None

    def test_post_request(self):
        response = self.client.post(self.url, model_to_dict(self.author))
        self.assertEqual(response.status_code, 200)


class AuthorUpdateViewTestCase(TestCase, BaseViewTestCaseMixin):

    @classmethod
    def setUpTestData(cls):
        cls.view = AuthorUpdateView
        cls.author = baker.make(Author)
        cls.url = f'/library/authors/{cls.author.author_id}/update'
        cls.url_name = 'author_update'
        cls.template_name = 'author_update.html'
        cls.context = {'author_id': cls.author.author_id}

    def test_post_request(self):
        response = self.client.post(self.url, model_to_dict(self.author), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='author_detail')


class BookUpdateViewTestCase(TestCase, BaseViewTestCaseMixin):
    @classmethod
    def setUpTestData(cls):
        cls.view = BookUpdateView
        cls.book = baker.make(Book)
        cls.url = f'/library/books/{cls.book.book_id}/update'
        cls.url_name = 'book_update'
        cls.template_name = 'book_update.html'
        cls.context = {'book_id': cls.book.book_id}

    def test_post_request(self):
        response = self.client.post(self.url, model_to_dict(self.book), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(template_name='book_detail')
