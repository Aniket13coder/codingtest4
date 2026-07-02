class Book:
    def __init__(self,title,author,is_borrowed= False):
        self.title= title
        self.author= author
        self.is_borrowed= is_borrowed
    def borrow(self):
        is_borrowed= True
        print(f'The book {self.title} has been borrowed.')
        return is_borrowed
    def return_book(self):
        is_borrowed= False
        print(f'The book {self.title} has been returned')
        return is_borrowed
    def display(self):
        print('The name of the book is: ',self.title)
book1= Book('Harry Potter and the Philosophers Stone','JK Rowling')
book2= Book('Harry Potter and the Chamber of Secrets','JK Rowling')
book3= Book('Harry Potter and the Prisoner of Azkaban','JK Rowling') 
book1.borrow()
book1.return_book()
book2.borrow()
book2.return_book()
book3.borrow()
book3.return_book()
book1.display()
book2.display()
book3.display()