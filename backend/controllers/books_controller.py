from models.book import Book

def getBooks():
    for book in Book.getBooks():
        yield book.toJson()
