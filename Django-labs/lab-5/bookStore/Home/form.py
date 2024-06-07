from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author_name' , 'genre' , 'title' , 'description' , 'rate' , 'views' ]
