from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("create-book/", views.createBook, name="create-book"),
    path("update-book/<int:id>/", views.updateBook, name="update-book"),
    path("delete-book/<int:id>/", views.deleteBook, name="delete-book"),
    path("show-book/<int:id>/", views.showBook, name="show-book"),
]
