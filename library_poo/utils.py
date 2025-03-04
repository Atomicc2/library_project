import json


def check_information(obj):
        
        for k, v in obj.__dict__.items():
            print(f"{k}: {v}")

'''def save_data(self):
    books_dict = [book.to_dict() for book in self.books]
    members_dict = [member.to_dict() for member in self.members]
    with open(f"data/{self.name}_books.json", "w") as book_file:
        json.dump(books_dict, book_file)
    with open(f"data/{self.name}_members.json", "w") as member_file:
        json.dump(members_dict, member_file)
    
def load_data(self):
    try:
        with open(f"data/{self.name}_books.json", "r") as book_file:
            self.books = json.load(book_file)
        with open (f"data/{self.name}_members.json", "r") as member_file:
            self.members = json.load(member_file)
    except FileNotFoundError:
        print("File not found")'''

