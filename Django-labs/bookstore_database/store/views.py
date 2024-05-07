from django.shortcuts import render, redirect
from .models import Book

# Create your views here.


def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "store/home.html", context)


def showBook(request, id):

    book = Book.objects.get(id=id)

    context = {"book": book}

    return render(request, "store/book-detail.html", context)


def createBook(request):

    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        rate = request.POST.get("rate")
        views = request.POST.get("views")

        book = Book(title=title, desc=desc, rate=rate, views=views)
        book.save()

    return redirect("home")


def updateBook(request, id):

    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.desc = request.POST.get("desc")
        book.rate = request.POST.get("rate")
        book.views = request.POST.get("views")

    book.save()

    return redirect("home")


def deleteBook(request, id):

    book = Book.objects.get(id=id)

    if request.method == "POST":
        book.delete()

    return redirect("home")
