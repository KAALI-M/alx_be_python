class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked = False
    def check_out_book(self):
        self._is_checked = True
    def return_book(self):
        self._is_checked = False
    def availability(self):
        return not(self._is_checked)

class Library:
    def __init__(self):
        self._books: list[Book] = []
    def add_book(self,book):
        self._books.append(book)

    def search_book(self,list, title):  # to filter 
        for index,book in enumerate(self._books):
            if book.title == title: # the book exists
                return index 
        return None

    def check_out_book(self,title):
        index =self.search_book(self._books, title)
        if index == None:
            return None
        else:
            self._books[index].check_out_book()
            return index
       
    def return_book(self,title):
        index =self.search_book(self._books, title)
        if index == None:
            return None
        else: #the book is available
            self._books[index].return_book()
            return index
    def list_available_books(self):
        for bk in self._books:
            if bk.availability()==True:
                print(f"\n{bk.title} by {bk.author}")

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))


    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
