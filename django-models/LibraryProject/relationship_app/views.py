# Implement Function-based View:

# Create a function-based view in relationship_app/views.py that lists all books stored in the database.
# This view should render a simple text list of book titles and their authors.
# Implement Class-based View:

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
# Configure URL Patterns:

# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

from django.shortcuts import render,
from django.http import HttpResponse
from .models import Library
from django.views.generic.detail import DetailView


def list_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return render(request, "relationship_app/list_books.html", {"books": books})
# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # you must create this template
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context 

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Change to your actual homepage view name
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

# Register View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Change to your actual homepage view name
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
