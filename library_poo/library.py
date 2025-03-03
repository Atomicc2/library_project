#Functions Library
from book import Book


class Library:
    
    def __init__(self):
        self.name = "Andinho's Library"
        self.books = []
        self.members = []

    def register_book(self, obj):
        self.books.append(obj)
        print(f"The book '{obj.title}' adicioned")
    
    def list_books(self):
        for i in self.books:
            print(f"{i.title}")
        
    def register_member(self, member):
        self.members.append(member)
        member.id = len(self.members)
        print(f"A new member '{member.name}' registered, id = {member.id}")
            
    def list_member(self):
        for i in self.members:
            print(f"{i.name}")
    
    def check_availability(self, name_book):
        for i in self.books:
            if i.title == name_book:
                pass