from itertools import chain

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic

from .forms import *
from .models import *


class IndexPage(View):
    def get(self, request):
        count_books = Book.objects.all().count()
        count_authors = Author.objects.all().count()
        return render(request, 'index.html', {'count_books': count_books,
                                              'count_authors': count_authors,
                                              })


class SearchResultView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        books = Book.objects.filter(Q(title__startswith=search_query) | Q(isbn__contains=search_query))
        authors = Author.objects.filter(Q(name__startswith=search_query) | Q(surname__startswith=search_query))
        results = chain(books, authors)
        print(results)
        return render(request, 'search_results.html', {'results': results,
                                                       })


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors.html'
    paginate_by = 5


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
        return render(request, 'author_create.html', {'author_form': author_form,
                                                      })

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
        return render(request, 'author_create.html', {'author_form': author_form,
                                                      })


class BookListView(generic.ListView):
    model = Book
    template_name = 'books.html'
    paginate_by = 5


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, book_id=book_id)
        return render(request, 'book_detail.html', {'book': book,
                                                    })


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
        return render(request, 'book_create.html', {'book_form': book_form,
                                                    })


class BookUpdateView(View):
    def get(self, request, book_id):
        book = Book.objects.get(book_id__exact=book_id)
        book_form = BookForm(instance=book)
        return render(request, 'book_update.html', {'book_form': book_form,
                                                    'book': book_form,
                                                    })

    def post(self, request, book_id):
        book = Book.objects.get(book_id__exact=book_id)
        book_form = BookForm(request.POST, instance=book)
        if book_form.is_valid():
            new_book = book_form.save()
            return redirect(new_book)
        return render(request, 'book_update.html', {'book_form': book_form,
                                                    'book': book_form,
                                                    })


class AuthorUpdateView(View):
    def get(self, request, author_id):
        author = Author.objects.get(author_id__exact=author_id)
        author_form = AuthorForm(instance=author)
        return render(request, 'author_update.html', {'author_form': author_form,
                                                      'author': author,
                                                      })

    def post(self, request, author_id):
        author = Author.objects.get(author_id__exact=author_id)
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            new_author = author_form.save()
            return redirect(new_author)
        return render(request, 'author_update.html', {'author_form': author_form,
                                                      'author': author,
                                                      })


class AuthorDeleteView(View):
    def get(self, request, author_id):
        author = Author.objects.get(author_id__exact=author_id)
        return render(request, 'author_delete.html', {'author': author})

    def post(self, request, author_id):
        author = Author.objects.get(author_id__exact=author_id)
        author.delete()
        return redirect(reverse('authors'))
