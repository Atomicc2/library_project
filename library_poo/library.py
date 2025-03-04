#Functions Library
from book import Book
from member import Member
import json


class Library:
    
    def __init__(self):
        self.name = "library1"
        self.books = []
        self.members = []

    def register_book(self, obj):
        self.books.append(obj)
        print(f"The book '{obj.title}' adicioned")
        self.save_data()
    
    def list_books(self):
        for i in self.books:
            print(f"{i.title}")
    
    def save_data(self):
        # Convert each object in the book and members list to a dictionary
        books_dict = [book.to_dict() for book in self.books]
        members_dict = [member.to_dict() for member in self.members]

        with open(f"data/{self.name}_books.json", "w") as book_file:
            json.dump(books_dict, book_file)
        with open(f"data/{self.name}_members.json", "w") as member_file:
            json.dump(members_dict, member_file)
    
    def load_data(self):
        try:
            with open(f"{self.name}_books.json", "r") as book_file:
                self.books = json.load(book_file)
            with open (f"{self.name}_members.json", "r") as member_file:
                self.members = json.load(member_file)
        except FileNotFoundError:
            print("File not found")

    def check_availability(self, name_book):
        self.load_data()
        for i in self.books:
            if i.title == name_book:
                if i.status:
                    return True
                else:
                    return False
            return
        print(f"The book {name_book} was not found!")
            
    def register_member(self, member):
        self.members.append(member)
        member.id = len(self.members)
        print(f"A new member '{member.name}' registered, id = {member.id}")
        self.save_data()
            
    def list_member(self):
        for i in self.members:
            print(f"{i.name}")