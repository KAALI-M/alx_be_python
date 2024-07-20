class Book:
    def __init__(self,title,author):
        self.author = author
        self.title = title
    def __str__(self):
        return f"book {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size:int = file_size
    def __str__(self):
        return f"book {self.title} by {self.author} size: {self.file_size}"
class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count : int = page_count
    def __str__(self):
        return f"book {self.title} by {self.author} pages: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.Books.append(book)
    def list_books(self):
        for index,book in enumerate(self.Books):
            print(book)

#lib = Library()
#eBook = EBook('python is good',"kAALI", 100)
#book= Book("hydraulic gates", "david louiz")
#pbook = PrintBook("monkeys will gouvern", "monkey", 240)

#lib.add_book(eBook)
#lib.add_book(book)
#lib.add_book(pbook)
#lib.list_books()