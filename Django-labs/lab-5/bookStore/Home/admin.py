from django.contrib import admin
from Home.models import Book
from django.contrib import admin
from Home.models import Isbn , Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('author_name' , 'rate' , 'views' , 'isbn' , 'category' , 'user')

admin.site.register(Isbn)
admin.site.register(Category)
