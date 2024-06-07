# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from Home.models import Book
from .form import BookForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login')
def index(request):
    books = Book.objects.all().values()
    return render(request, "home/index.html", {"books": books})

@login_required(login_url='/user/login')
def show(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "home/show.html", {"book": book})

@login_required(login_url='/user/login')
def edit(request, id):

    book = Book.objects.get(pk=id)
    form = BookForm(instance=book)
    return render(request, "home/edit.html", {'form':form , 'book':book})

@login_required(login_url='/user/login')
def create(request):

    form = BookForm()
    return render(request, "home/create.html" , {"form" : form})

@login_required(login_url='/user/login')
def store(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Assign the current user to the book
            book.save()
            return redirect('BookStore:book-index')
        else:
            print(form.errors)
    else:
        form = BookForm()
    return render(request, "home/create.html", {"form": form})

@login_required(login_url='/user/login')
@csrf_protect
def update(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():  # Call is_valid() as a function
        form.save()

    return redirect("BookStore:book-index")



@login_required(login_url='/user/login')
def destroy(request, id):

    book = Book.objects.get(pk=id)
    book.delete()
    return redirect("BookStore:book-index")
