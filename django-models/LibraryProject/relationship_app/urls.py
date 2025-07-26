from django.urls import path
from .views import   list_books, LibraryDetailView,login_view, logout_view,register_view


urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
      path('admin-view/', admin_view, name='admin_view'),
]


from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
from django.urls import path, include


from django.urls import path
from . import views

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]

from django.urls import path
from .views import register_view, login_view, logout_view, list_books, LibraryDetailView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # other URLs
]

from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]

