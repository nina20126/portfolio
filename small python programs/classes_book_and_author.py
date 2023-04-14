'''
Author - Book (note: association)

Put min 2 attributes to all classes.

Then methods that are needed

Remember relationships between classe
'''

class Author:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.books = []

    def get_author_info(self):
        author_info = f"{self.name} (born {self.birth}). List of books: {self.books}"
        return author_info

    def addBook(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, released, author):
        self.title = title
        self.released = released
        self.author = author
        
    def set_author(self, auth):
        self.author = auth

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author

    def get_book_info(self):
        book_info = f"{self.title} ({self.released})"
        return book_info

author1 = Author("Stephen King", 1947)
author2 = Author("Dean Koontz", 1945)
author3 = Author("Anne Rice", 1941)

book1 = Book("The Shinig", 1975, author1)
book2 = Book("Cujo", 1981, author1)
book3 = Book("Salem's Lot", 1975, author1)
book4 = Book("Weird World", 1986, author2)
book5 = Book("Terra Phobia", 1973, author2)
book6 = Book("Interview with the Vampire", 1976, author3)
book7 = Book("The vampire Lestat", 1985, author3)
book8 = Book("Queen of the damned", 1988, author3)

author1.addBook(book1.get_title())
author1.addBook(book2.get_title())
author1.addBook(book3.get_title())
author2.addBook(book4.get_title())
author2.addBook(book5.get_title())
author3.addBook(book6.get_title())
author3.addBook(book7.get_title())
author3.addBook(book8.get_title())

print(author1.get_author_info())
print(book4.author.get_author_info())
author3.addBook("The tale of the body thief")
print(author3.get_author_info())
