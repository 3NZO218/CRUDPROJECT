from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'user', 'body', 'price', 'rating', 'pub_date', 'publisher', 'author']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
        }
