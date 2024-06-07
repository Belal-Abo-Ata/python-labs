from django.shortcuts import render, redirect

# Create your views here.


books = [
    {
        "id": 1,
        "name": "Head First Design Pattern",
        "desc": "This is book description",
        "image": "https://placehold.co/400x400/orange/white",
    },
    {
        "id": 2,
        "name": "Head First Java",
        "desc": "This is book description",
        "image": "https://placehold.co/400x400/tomato/white",
    },
    {
        "id": 3,
        "name": "Head First Python",
        "desc": "This is book description",
        "image": "https://placehold.co/400x400/purple/white",
    },
]


def home(request):
    context = {"books": books}
    return render(request, "base/home.html", context)


def showBook(request, id):
    context = {}

    for book in books:
        if book["id"] == id:
            context = {"book": book}
            break
    return render(request, "base/book-detail.html", context)


def createBook(request):

    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        books.append(
            {
                "id": max(book["id"] for book in books) + 1,
                "name": name,
                "desc": desc,
                "image": "https://placehold.co/400x400/green/white",
            }
        )

        print(books)

    return redirect("home")


def updateBook(request, id):

    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")

        for book in books:
            if book["id"] == id:
                book["name"] = name
                book["desc"] = desc
                break

    return redirect("home")


def deleteBook(request, id):

    i = 0
    while i < len(books):
        if books[i].get("id") == id:
            del books[i]
            break
        else:
            i += 1

    return redirect("home")
