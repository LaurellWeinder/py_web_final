from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic

from .forms import *
from .models import *


class IndexPage(View):
    def get(self, request):
        count_books = Book.objects.all().count()
        count_authors = Author.objects.all().count()
        return render(request, 'index.html', {'count_books': count_books,
                                              'count_authors': count_authors
                                              },
                      )


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors.html'


class AuthorDetailView(View):
    def get(self, request, author_id):
        author = get_object_or_404(Author, author_id=author_id)
        if author:
            author_books = Book.objects.all().filter(author_id=author_id)
        else:
            raise ValueError('No books of this author')
        return render(request, 'author_detail.html', {'author': author,
                                                      'author_books': author_books,
                                                      })


class AuthorCreateView(View):
    def get(self, request):
        author_form = AuthorForm()
        return render(request, 'author_create.html', {'author_form': author_form})

    def post(self, request):
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            qs = Author.objects.filter(name=author_form.cleaned_data['name'],
                                       surname=author_form.cleaned_data['surname'],
                                       )
            if not qs.exists():
                new_author = author_form.save()
                return redirect(new_author)
            else:
                messages.error(request, 'This author already exists')
        return render(request, 'author_create.html', {'author_form': author_form})


class BookListView(generic.ListView):
    model = Book
    template_name = 'books.html'


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, book_id=book_id)
        return render(request, 'book_detail.html', {'book': book})


class BookCreateView(View):
    def get(self, request):
        book_form = BookForm()
        return render(request, 'book_create.html', context={'book_form': book_form,
                                                            })

    def post(self, request):
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            qs = Book.objects.filter(isbn=book_form.cleaned_data['isbn'])
            if not qs.exists():
                new_book = book_form.save()
                return redirect(new_book)
            else:
                messages.error(request, 'This book already exists')
        return render(request, 'book_create.html', {'book_form': book_form})
