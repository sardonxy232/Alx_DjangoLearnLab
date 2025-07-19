# Show current books before deletion
print("Books before deletion:")
for book in Book.objects.all():
    print(f"- {book}")

print(f"Total books before deletion: {Book.objects.count()}")

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"\nDeleting book: {book}")
book.delete()

# Confirm deletion
print(f"\nTotal books after deletion: {Book.objects.count()}")

print("Books after deletion:")
for book in Book.objects.all():
    print(f"- {book}")

# Verify deletion by trying to retrieve
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
    print("Book still exists!")
except Book.DoesNotExist:
    print("Confirmed: Book successfully deleted")