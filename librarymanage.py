class library:
    def __init__(self):
       self.noBooks= 0
       self.books = []
       
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
    def showInfo(self):
        print(f"The library has {self.noBooks} books.The books are")
        for books in self.books:
            print(books)

l1 = library()
l1.addBook("The Alchamist")
l1.addBook("Harry potter")
l1.addBook("Thousand of leagues under the sea")
l1.addBook("Sherlock Holmes")
l1.addBook("The prophet")
l1.addBook("Inferno")
l1.addBook("Mr. jackely and Mr. Hide")
l1.addBook("Padma nodir majhi")

l1.showInfo()