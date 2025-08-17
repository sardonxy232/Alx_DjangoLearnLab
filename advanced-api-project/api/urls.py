from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),          # GET all books
    path("books/create/", BookCreateView.as_view(), name="book-create"), # POST new book
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"), # GET, PUT, PATCH, DELETE single book
]
