#Functions Library
from book import Book
from member import Member
from os import path
from json import dump, load


class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def save_books(self):
        books_dict = [book.to_dict() for book in self.books]
        with open(f"data/{self.name}_books.json", 'w') as file:
            dump(books_dict, file, indent=4)

    def save_members(self):
        members_dict = [member.to_dict() for member in self.members]
        with open(f"data/{self.name}_members.json", 'w') as file:
            dump(members_dict, file, indent=4)

    def load_books(self):
        books_path = f"data/{self.name}_books.json"
        if path.exists(books_path):
            with open(books_path, 'r') as book:
                data_books = load(book)
                self.books = [Book(**item) for item in data_books]
    
    def load_members(self):
        members_path = f"data/{self.name}_members.json"
        if path.exists(members_path):
            with open(members_path, 'r') as member:
                data_members = load(member)
                self.members = [Member(**item) for item in data_members]

    def register_book(self, obj):
        self.books.append(obj)
        print(f"The book '{obj.title}' adicioned")
        self.save_books()

    def list_books(self):
        self.load_books()
        for i in self.books:
            print(f"{i.title}: {i.status}")
    
    def check_availability(self, name_book):
        self.load_books()
        for i in self.books:
            if i.title == name_book:
                return i.status
        print(f"The book {name_book} was not found!")
            
    def register_member(self, member):
        self.members.append(member)
        member.id = len(self.members)
        print(f"A new member '{member.name_user}' registered, id = {member.id}")
        self.save_members()

    def list_members(self):
        self.load_members()
        for i in self.members:
            print(f"{i.name_user}")

    def set_availability(self, title):
        for i in self.books:
            if i.title == title:
                i.status = not i.status
        self.save_books()    