from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/create', BookCreateView.as_view(), name='book_create'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/create', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:author_id>', AuthorDetailView.as_view(), name='author_detail')
]
