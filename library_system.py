class Book:
    def __init__(self, title, author, pages):
        self.title= title
        self.author= author
        self.pages= pages
        self.borrowed= False

    def __str__(self):
            status= "borrowed" if self.borrowed else "Available"
            return f'"{self.title}" by {self.author} [{status}]'
        
    def __len__(self):
         return self.pages
    
class Library:
     def __init__ (self, name):
          self.name = name
          self.books= []

     def add_book(self, book):
          self.books.append(book)
          print(f"Added: {book.title}")

     def find_book(self, title):
        for book in self.books:
          if book.title.lower() == title.lower():
               return book
          return None
     
     def borrow_book(self, title):
          book= self.find_book(title)
          if book is None:
               print("Book not found!")
          elif book.borrowed:
               print(f'"{title}" is already borrowed.')
          else:
               book.borrowed = True 
               print(f'Borrowed: "{title}"')

     def catalogue(self):
        print(f"\n=== {self.name} ===")
     for book in self.books:
          print(" ", book)
          
     

