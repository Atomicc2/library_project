class Member:
    
    def __init__(self, name_user='<unknown>', id=0, book_count=0):
        self.name_user = name_user
        self.id = id
        self.book_count = book_count
        self.borrowed_books = []

    def to_dict(self):
        #Return the member formatted for dictionary
        return {
            'name_user': self.name_user,
            'id': self.id,
            'book_count': self.book_count,
        }

    def borrow_book(self, title):
        #Add the book to your borrowed books and update count list
        self.borrowed_books.append(title)
        self.book_count += 1
    
    def returne_book(self, title):
        #Remove the book to your borrowed books
        self.borrowed_books.remove(title)
