from django.db import models
from django.urls import reverse
from .validators import has_no_numbers, check_year

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, validators=[has_no_numbers])
    surname = models.CharField(max_length=50, validators=[has_no_numbers])

    class Meta:
        ordering = ['-author_id']

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'author_id': self.author_id})

    def __str__(self):
        return f'{self.surname} {self.name}'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField(validators=[check_year])
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=50)

    class Meta:
        ordering = ['-book_id']

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.book_id})

    def __str__(self):
        return f'{self.title} - {self.author}'
