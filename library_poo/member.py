from utils import *

class Member:
    
    def __init__(self, name="<unknown>", id=0, book_count=0):
        self.name = name
        self.id = id
        self.book_count = book_count
    
    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'book_count': self.book_count
        }

    