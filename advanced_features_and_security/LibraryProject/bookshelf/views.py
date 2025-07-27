from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm


# Use Django ORM filtering to prevent SQL injection


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, description=description, published_date=published_date)
        return redirect('book_list')
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def book_search_view(request):
    form = BookSearchForm(request.GET or None)
    books = []
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)
    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})
