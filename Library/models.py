from django.db import models
from django.urls import reverse


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_id': self.author_id})

    def __str__(self):
        return f'{self.surname} {self.name}'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.book_id})

    def __str__(self):
        return f'{self.title} - {self.author}'
