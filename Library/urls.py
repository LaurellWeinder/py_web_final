from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/create', BookCreateView.as_view(), name='book_create'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:book_id>/update', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:book_id>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/create', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<int:author_id>/update', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:author_id>/delete', AuthorDeleteView.as_view(), name='author_delete'),
]
