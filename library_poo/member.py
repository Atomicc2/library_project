from utils import input_str, input_int

class Member:
    
    def __init__(self, name_user='<unknown>', id=0, book_count=0, borrowed_books = [], age=0):
        self.name_user = name_user
        self.id = id
        self.book_count = book_count
        self.borrowed_books = borrowed_books
        self.age = age

    def to_dict(self):
        #Return the member formatted for dictionary
        return {
            'name_user': self.name_user,
            'id': self.id,
            'book_count': self.book_count,
            'borrowed_books': self.borrowed_books,
            'age': self.age
        }

    def new_member(self):
        while True:
            self.name_user = input_str("What's the your name? ")
            self.age = input_int("What's is the your age? ")
            print(f"A new member {self.name_user} added!")
            break