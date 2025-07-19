# Retrieve the book
book = Book.objects.get(title="1984")

# Display current title
print(f"Current title: {book.title}")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Display updated title
print(f"Updated title: {book.title}")

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(f"Verified title from database: {updated_book.title}")