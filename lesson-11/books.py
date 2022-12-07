with open('books.txt') as books_file:
    for book in books_file:
        book = book.strip()
        print(book)