from utils import *

class Book:

    def __init__(self, title='<unknown>', author='unknown', gender='indefined', number_pages=0):
        self.title = title
        self.author = author
        self.gender = gender
        self.number_pages = number_pages
    
    def to_dict(self):
        return{
            'title': self.title,
            'author': self.author,
            'gender': self.gender,
            'number_pages': self.number_pages
        }
    
    