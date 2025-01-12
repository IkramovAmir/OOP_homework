class Book:
    def __init__(self, name = None, due_date = None) -> None:
        self.name = name
        self.due_date = due_date
        
    def borrower(self):
        self.name = input("\nEnter name: ")
        self.due_date = int(input("Enter day: "))
        books.append(self)
    
    def returning_book(self):
        self.name = input("\nEnter your name: ")
        for book in books:
            if book.name == self.name:
                books.remove(book)
                print("\nBorrower removed successfully!!!")
            else:
                print('Borrower is not found!')
    

books = []
n = 0    
while n != 3:
    print("\nTo borrow book enter - 1",
          "To return book enter - 2",
          "To exit program enter - 3", sep="\n")
    n = int(input("\nYour choice-> "))
    
    if n == 1:
        book = Book()
        book.borrower()
    
    if n == 2:
        remove = Book()
        remove.returning_book()
    
    for book in books:
        print(f"{book.name} {book.due_date}")

print("\nThanks to use our program!")