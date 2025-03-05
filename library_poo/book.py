from utils import input_str, input_int

class Book:

    def __init__(self, title='<unknown>', author='unknown', genre='indefined', number_pages=0, status=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.number_pages = number_pages
        self.status = status
    
    def to_dict(self):
      #Return the book formatted for dictionary
      return {
          'title': self.title,
          'author': self.author,
          'genre': self.genre,
          'number_pages': self.number_pages,
          'status': self.status,
      }
    
    def new_book(self):
        while True:
            print("Add the information of book!")
            self.title = input_str("Title: ")
            self.author = input_str("Author: ")
            self.genre = input_str("Genre: ")
            self.number_pages = input_int("Number of pages: ")
            print(f"A new book {self.title} is added!")
            break
