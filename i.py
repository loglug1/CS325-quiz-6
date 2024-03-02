from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    genre: str

class Catalog:
    def set_catalog(self, catalog: list[Book]):
        self.catalog = catalog

class CatalogManager(Catalog):
    def add_book(self, book: Book):
        self.catalog.append(book)
    
    def remove_book(self, book: Book):
        self.catalog.remove(book)

class CatalogUser(Catalog):
    def find_author(self, author: str):
        lst = list()
        for book in self.catalog:
            if author in book.author:
                lst.append(book)
        return lst

    def find_title(self, title: str):
        lst = list()
        for book in self.catalog:
            if title in book.title:
                lst.append(book)
        return lst

    def find_genre(self, genre: str):
        lst = list()
        for book in self.catalog:
            if genre in book.genre:
                lst.append(book)
        return lst

class BookBorrower:
    borrowed_books: list[Book] = list()

    def check_out_book(self, book: Book, manager: CatalogManager):
        manager.remove_book(book)
        self.borrowed_books.append(Book)
    
    def return_book(self, book: Book, manager: CatalogManager):
        self.borrowed_books.remove(Book)
        manager.add_book(book)


class Patron(CatalogUser, BookBorrower):
    def __init__(self, catalog: list[Book]):
        self.set_catalog(catalog)

class Librarian(CatalogUser, CatalogManager):
    def __init__(self, catalog: list[Book]):
        self.set_catalog(catalog)


def main():
    catalog = [Book("The Hunger Games", "Suzanne Collins", "dystopian fiction"), Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "fantasy fiction")]

    librarian = Librarian(catalog)
    patron1 = Patron(catalog)
    patron2 = Patron(catalog)

    search = patron1.find_title("Harry Potter")
    patron1.check_out_book(search[0], librarian)
    patron1.return_book(patron1.borrowed_books[0], librarian)

    search = patron2.find_genre("fiction")
    patron2.check_out_book(search[1], librarian)


if __name__=="__main__":
    main()