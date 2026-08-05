class book:
    def __init__(self,title,authour):
        self.title=title
        self.authour=authour
        self.is_borrowed=False 

class ebook(book):
    def __init__(self,title,authour,file_size):
        super(). __init__(title,authour)
        self.file_size=file_size

class libray:
    def __init__(self):
        self.books =[]
    def add_book(self,book):
        self.books.append(book)

    def borrow_book(self,title):
        for book in self.books:
            if book.title==title:
                if book .is_borowed:
                    raise Exception("book is alerdy borrowed")
                book.is_borrowed=True
                return   
            
    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.is_borrowed = False
                return
    def list_avialable(self):
        for book in self.books:
            if not book.is_borrowed:
                print(book.title)


la =libray()
b1=book("4a","2b",)
b2=ebook("a","h","bh")
la.add_book(b1)
la.add_book(b2)

la.list_avialable()
la.borrow_book("a")
la.list_avialable()
la.borrow_book("h")

                                             