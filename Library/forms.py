from django import forms

from Library.models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'year', 'publisher']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'author': forms.Select(attrs={'class': 'form-control'}),
                   'isbn': forms.TextInput(attrs={'class': 'form-control'}),
                   'year': forms.NumberInput(attrs={'class': 'form-control'}),
                   'publisher': forms.TextInput(attrs={'class': 'form-control'}),
                   }




class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'surname': forms.TextInput(attrs={'class': 'form-control'}),
                   }
