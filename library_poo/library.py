#Functions Library
from json import dump, load, JSONDecodeError
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
                    if data_members:
                        self.members = [Member(**i) for i in data_members]
                    else:
                        print("No members found in this file!")
            else:
                print("Member file does not exist!")
        except JSONDecodeError:
            print("Error, file is empty or corrupt!")

    def register_book(self, obj):
        #Register a new book
        self.books.append(obj)
        self.save_books()

    def list_books(self):
        #List the books
        self.load_books()
        for i in self.books:
            print(f"{i.title}:\t{'Available' if i.status == True else 'Unavailable!'}")
    
    def register_member(self, member):
        #register a new member 
        self.members.append(member)
        member.id = len(self.members)
        self.save_members()

    def list_members(self):
        #List the members
        self.load_members()
        for i in self.members:
            print(f"Name:{i.name_user}\tId:{i.id}")

    def set_availability(self, title):
        #Set statues to false or true
        for i in self.books:
            if i.title == title:
                i.status = not i.status
        self.save_books()
        self.save_members()    

    def borrow_book(self):
        #Add the book to your borrowed books and update count list
        self.load_books()
        self.load_members()
        name_book = utils.input_str("Which book do you want to borrow? ")
        if self.verify_status(name_book):
            try:
                name_member = utils.input_str("Who will borrow? ")
                for i in self.members:
                    if i.name_user == name_member:
                        i.borrowed_books.append(name_book)
                        self.set_availability(name_book)
                        utils.menus(f"Good read {i.name_user}, {name_book} is a good book!")
                        break
                else:
                    print("Member not found!")
            except (ValueError, NameError):
                print("Error checking parameters!")
        else:
            print("Book not found or unavailable!")

    def return_book(self):
        #Return book, update status for True and remove from list borrowed_books
        name = utils.input_str("Who wants return the book? ")
        try: 
            if self.verify_member(name):
                book = utils.input_str("Which book do you want to return? ")
                if self.verify_book(book):
                    for member in self.members:
                        if book in member.borrowed_books:
                            member.borrowed_books.remove(book)
                            self.set_availability(book)
                            utils.menus(f"Thanks for the return {name}. I hope you enjoyed the book {book}")
                            break
                        else:
                            print("This member has not rented this book")
                else:
                    print("Book not found!")
            else:
                print("Member not found!")                         
        except ValueError:
            print("Erro in the return!")

    def verify_member(self, name):
        #Check this is member is registered
        self.load_members()
        for i in self.members:
            if i.name_user == name:
                return True
    
    def verify_status(self, name_book):
        #Check if the requested book is available
            self.load_books()
            for i in self.books:
                if i.title == name_book and i.status == True:
                    return True
                
    def verify_book(self, title):
        #Check this is book is registered
        self.load_books()
        for i in self.books:
            if i.title == title:
                return True
    
    def show_status(self):
        #Show availability the book
        book = utils.input_str("Which book do you want to check? ")
        if self.verify_status(book):
            print("This book is available!")
        else:
            print("This book is unavailable!")
     
    def exit_library(self):
        #Exit program
        utils.menus("Bye Bye, see you later!")
        self.save_books()
        self.save_members()
        exit()