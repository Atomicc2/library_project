#Functions Library
from json import dump, load
from os import path

from book import Book
from member import Member
import utils


class Library:
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def save_books(self):
        #Add book to list json
        books_dict = [book.to_dict() for book in self.books]
        with open(f"data/{self.name}_books.json", 'w') as file:
            dump(books_dict, file, indent=4)

    def save_members(self):
        #Add member to list json
        members_dict = [member.to_dict() for member in self.members]
        with open(f"data/{self.name}_members.json", 'w') as file:
            dump(members_dict, file, indent=4)

    def load_books(self):
        #Return the updated list of books for the attributes
        try:
            books_path = f"data/{self.name}_books.json"
            if path.exists(books_path):
                with open(books_path, 'r') as book:
                    data_books = load(book)
                    self.books = [Book(**i) for i in data_books]
        except FileNotFoundError:
            print("ERRO! File not found!")
    
    def load_members(self):
        #Return the updated list of members for the attributes
        try:
            members_path = f"data/{self.name}_members.json"
            if path.exists(members_path):
                with open(members_path, 'r') as member:
                    data_members = load(member)
                    self.members = [Member(**i) for i in data_members]
        except FileNotFoundError:
            print("ERRO! File not found!")
            self.members = []
            self.save_members()

    def register_book(self, obj):
        #Register a new book
        self.books.append(obj)
        self.save_books()

    def list_books(self):
        #List the books
        self.load_books()
        for i in self.books:
            print(f"{i.title}: {'Available' if i.status == True else 'Unavailable!'}")
    
    def check_availability(self, msg):
        #Check if the requested book is available
            name_book = utils.input_str(msg)
            self.load_books()
            for i in self.books:
                if i.title == name_book:
                    return i.status, name_book
            
    def register_member(self, member):
        #register a new member 
        self.members.append(member)
        member.id = len(self.members)
        self.save_members()

    def list_members(self):
        #List the members
        self.load_members()
        for i in self.members:
            print(f"Name:{i.name_user} - Id:{i.id}")

    def set_availability(self, title):
        #Set statues to false or true
        for i in self.books:
            if i.title == title:
                i.status = not i.status
        self.save_books()    

    def borrow_book(self):
        #Add the book to your borrowed books and update count list
        resp = self.check_availability("Which book do you want to borrow? ")
        if resp[0] == True:
            name = utils.input_str("Who will borrow the book? ")
            for i in self.members:
                if i.name_user == name:
                    i.borrowed_books.append(resp[1])
                    i.book_count += 1
                    self.set_availability(resp[1])
                    print(f"The member {i['name_user']} just borrowed the book {resp[1]}")
                    break
                else:
                    print("User not found!")
        else:
            print("This book is unavailable!")
                    