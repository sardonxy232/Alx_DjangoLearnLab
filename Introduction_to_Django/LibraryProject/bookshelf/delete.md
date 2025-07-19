# delete.md

# Delete the book entry
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()

# Confirm the deletion
>>> Book.objects.filter(title="Nineteen Eighty-Four").exists()
False
